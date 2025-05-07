#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Real-time YOLOv8-face detector on the IMX500 using Picamera2.
Now uses the xywh2xyxy / compute_iou / nms utilities provided by the user.
"""

import time
import cv2
import numpy as np
from picamera2 import Picamera2, MappedArray
from picamera2.devices import IMX500
from picamera2.devices.imx500 import NetworkIntrinsics

# ------------------------------------------------------------------
# USER UTILITIES  (either paste here or `from utils import xywh2xyxy, nms`)
# ------------------------------------------------------------------
def xywh2xyxy(xywh):
    x, y, w, h = xywh[:, 0], xywh[:, 1], xywh[:, 2], xywh[:, 3]
    x1 = x - w / 2
    y1 = y - h / 2
    x2 = x + w / 2
    y2 = y + h / 2
    return np.stack([x1, y1, x2, y2], axis=1)

def compute_iou(box1, box2):
    x11, y11, w1, h1 = box1
    x21, y21, w2, h2 = box2
    x12, y12 = x11 + w1, y11 + h1
    x22, y22 = x21 + w2, y21 + h2
    xI1, yI1 = max(x11, x21), max(y11, y21)
    xI2, yI2 = min(x12, x22), min(y12, y22)
    inter = max(0, xI2 - xI1) * max(0, yI2 - yI1)
    union = w1 * h1 + w2 * h2 - inter + 1e-6
    return inter / union

def nms(xywh, scores, iou_threshold=0.5):
    order = np.argsort(scores)[::-1]
    keep = []
    while order.size:
        i = order[0]
        keep.append(i)
        order = order[1:]
        ious = np.array([compute_iou(xywh[i], xywh[j]) for j in order])
        order = order[ious < iou_threshold]
    return np.array(keep)

# ------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------
MODEL_PATH = "/home/user/packDemo3/network.rpk"          # compiled rpk from yolov8n-face
LABELS     = ["face"]
CONF_THR   = 0.5
IOU_THR    = 0.5
MAX_DETS   = 20

# ------------------------------------------------------------------
# IMX500 INITIALISATION
# ------------------------------------------------------------------
imx500 = IMX500(MODEL_PATH)
intr = imx500.network_intrinsics or NetworkIntrinsics()
intr.task, intr.labels = "object detection", LABELS
intr.update_with_defaults()

picam2 = Picamera2(imx500.camera_num)
cfg = picam2.create_preview_configuration(
    controls={"FrameRate": intr.inference_rate},
    buffer_count=12
)
picam2.start(cfg, show_preview=True)

MODEL_W, MODEL_H = imx500.get_input_size()

# ------------------------------------------------------------------
# DETECTION PIPELINE
# ------------------------------------------------------------------
def parse_detections(meta):
    """
    Return list of tuples:
        (box_xyxy_int, score_float, landmarks_or_None)
    where box_xyxy_int = (x1,y1,x2,y2).
    Handles both ‘YOLO-style’ (1-tensor) and ‘generic OD’ (3-tensor) RPks.
    """
    outs = imx500.get_outputs(meta, add_batch=True)
    if outs is None:
        return []

    if len(outs) == 1:
        # ─────────────  YOLO-style  ─────────────
        preds = outs[0].squeeze(0).T        # (20, N)
        conf  = preds[4, :]
        mask  = conf > CONF_THR
        if not np.any(mask):
            return []

        preds = preds[:, mask]
        conf  = conf[mask]
        xywh  = preds[:4, :].T                          # (M,4)
        lms   = preds[5:, :].T.reshape(-1, 5, 3)[:, :, :2]  # (M,5,2)
    else:
        # ─────────────  Generic object-detection layout  ─────────────
        # outs[0]: boxes (1,N,4); outs[1]: scores (1,N) or (1,N,C)
        xywh  = outs[0][0]                              # (N,4)
        scores = outs[1][0]
        # If scores has class dimension, take max
        if scores.ndim == 2:
            scores = scores.max(axis=1)
        conf  = scores
        lms   = None

        mask  = conf > CONF_THR
        if not np.any(mask):
            return []

        xywh  = xywh[mask]
        conf  = conf[mask]

    # ─────────────  NMS / keep top-K  ─────────────
    keep = nms(xywh, conf, IOU_THR)[:MAX_DETS]
    xywh, conf = xywh[keep], conf[keep]
    if lms is not None:
        lms = lms[keep]

    # ─────────────  scale to preview pixels  ─────────────
    ph, pw = picam2.stream_configuration("main")["size"][1], \
             picam2.stream_configuration("main")["size"][0]
    sx, sy = pw / MODEL_W, ph / MODEL_H
    boxes_xyxy = xywh2xyxy(xywh)
    boxes_xyxy[:, [0, 2]] *= sx
    boxes_xyxy[:, [1, 3]] *= sy
    if lms is not None:
        lms *= np.array([sx, sy])

    dets = []
    for i, box in enumerate(boxes_xyxy.astype(int)):
        dets.append((box, float(conf[i]),
                     None if lms is None else lms[i].astype(int)))
    return dets

# ------------------------------------------------------------------
# 3.  Drawing callback (skip landmarks if not present)
# ------------------------------------------------------------------
GREEN = (0, 255, 0)
RED   = (0,   0, 255)

def draw(req, stream="main"):
    for box, score, lm in parse_detections(req.get_metadata()):
        x1, y1, x2, y2 = box
        with MappedArray(req, stream) as m:
            cv2.rectangle(m.array, (x1, y1), (x2, y2), GREEN, 2)
            cv2.putText(m.array, f"{score:.2f}", (x1, y1 - 4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN, 1, cv2.LINE_AA)
            if lm is not None:            # YOLO-style model → 5 landmarks
                for lx, ly in lm:
                    cv2.circle(m.array, (lx, ly), 2, RED, -1)

picam2.pre_callback = draw
# ------------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------------
try:
    while True:
        picam2.capture_metadata()  # triggers pre_callback
        # time.sleep(0.005)
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
