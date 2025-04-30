import time
import cv2
from picamera2 import Picamera2, MappedArray
from picamera2.devices import IMX500
from picamera2.devices.imx500 import NetworkIntrinsics, postprocess_nanodet_detection

# Update these paths
MODEL_PATH = "network.rpk"
LABELS = ["face"]  # Only one class

# Load the model
imx500 = IMX500(MODEL_PATH)
intrinsics = imx500.network_intrinsics or NetworkIntrinsics()
intrinsics.task = "object detection"
intrinsics.labels = LABELS
intrinsics.update_with_defaults()

# Initialize camera
picam2 = Picamera2(imx500.camera_num)
config = picam2.create_preview_configuration(controls={"FrameRate": intrinsics.inference_rate}, buffer_count=12)

picam2.start(config, show_preview=True)

def parse_detections(metadata):
    outputs = imx500.get_outputs(metadata, add_batch=True)
    if outputs is None:
        return []

    input_w, input_h = imx500.get_input_size()

    if intrinsics.postprocess == "nanodet":
        boxes, scores, classes = postprocess_nanodet_detection(
            outputs=outputs[0],
            conf=0.4,
            iou_thres=0.5,
            max_out_dets=10
        )[0]
        detections = []
        for i in range(len(boxes)):
            x, y, w, h = boxes[i]
            conf = scores[i]
            cls = classes[i]
            detections.append((int(x), int(y), int(w), int(h), conf, int(cls)))
        return detections

    else:
        # Regular detection
        boxes = outputs[0][0]
        scores = outputs[1][0]
        classes = outputs[2][0]

        # Assume boxes are normalized if needed
        if intrinsics.bbox_normalization:
            # Scale to input size
            boxes = [[b * input_h for b in box] for box in boxes]

        # If bbox order is "xy", swap y and x
        if intrinsics.bbox_order == "xy":
            boxes = [[box[1], box[0], box[3], box[2]] for box in boxes]

        detections = []
        for i in range(len(scores)):
            if scores[i] < 0.4:
                continue
            x0, y0, x1, y1 = boxes[i]
            w = x1 - x0
            h = y1 - y0
            detections.append((int(x0), int(y0), int(w), int(h), scores[i], int(classes[i])))

        return detections



def draw_detections(request, stream="main"):
    detections = parse_detections(request.get_metadata())
    with MappedArray(request, stream) as m:
        for x, y, w, h, conf, cat in detections:
            label = f"{LABELS[cat]} ({conf:.2f})"
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(m.array, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Hook the draw function
picam2.pre_callback = draw_detections

try:
    while True:
        metadata = picam2.capture_metadata()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    picam2.stop()

