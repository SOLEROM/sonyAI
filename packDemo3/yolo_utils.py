import numpy as np

def xywh2xyxy(xywh):
    # Convert [x, y, w, h] -> [x1, y1, x2, y2]
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

    xI1, yI1, xI2, yI2 = max(x11, x21), max(y11, y21), min(x12, x22), min(y12, y22)

    inter_area = max(0, (xI2 - xI1)) * max(0, (yI2 - yI1))
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - inter_area + 1e-6

    return inter_area / union_area

def nms(xywh, scores, iou_threshold=0.5):
    sorted_indices = np.argsort(scores)[::-1]
    selected_indices = []
    while len(sorted_indices) > 0:
        best_idx = sorted_indices[0]
        selected_indices.append(best_idx)
        sorted_indices = sorted_indices[1:]

        iou = np.array([compute_iou(xywh[best_idx], xywh[i]) for i in sorted_indices])
        sorted_indices = sorted_indices[iou < iou_threshold]

    return np.array(selected_indices)