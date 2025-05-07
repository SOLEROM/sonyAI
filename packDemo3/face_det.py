import numpy as np
import cv2
import onnxruntime
from yolo_utils import nms, xywh2xyxy


class FaceDetector:
    def __init__(self, model_name):
        self.session = onnxruntime.InferenceSession(model_name)
        self.input_name = self.session.get_inputs()[0].name
        self.input_shape = self.session.get_inputs()[0].shape
    
    def preprocess(self, image):        
        x = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        x = cv2.resize(x, (640, 640))
        x = x.transpose(2, 0, 1) / 255.0
        x = np.expand_dims(x, axis=0).astype(np.float32)
        x = np.ascontiguousarray(x)        
        return x
        
    def postprocess(self, outputs, input_resolution, model_resolution,
                class_confidence_threshold=0.5, iou_threshold=0.5):
        """
        Postprocess YOLOv8-face ONNX output (shape: 8400, 20)
        """
        # Step 1: Extract and sigmoid the confidence column   
        confidence = outputs[4, :]  # confidence is in the 5th row
        # Step 2: Filter rows by confidence threshold
        mask = confidence > class_confidence_threshold
        if not np.any(mask):
            return np.array([]), np.array([]), np.array([])

        filtered_outputs = outputs[:, mask]
        confidence = confidence[mask]
        filtered_outputs = filtered_outputs.T
        xywh = filtered_outputs[:, :4]
        landmarks = filtered_outputs[:, 5:].reshape(-1, 5, 3)[:, :, :2]  # reshape to (N, 5, 2)

        keep_indices = nms(xywh, confidence, iou_threshold)
        if len(keep_indices) == 0:
            return np.array([]), np.array([]), np.array([])
        boxes_xyxy = xywh2xyxy(xywh)
        boxes = boxes_xyxy[keep_indices]#.numpy()
        confidence = confidence[keep_indices]#.numpy()
        landmarks = landmarks[keep_indices]#.numpy()]

        # Step 5: Scale boxes and landmarks to input resolution
        scale_x = input_resolution[1] / model_resolution[1]
        scale_y = input_resolution[0] / model_resolution[0]
        boxes[:, [0, 2]] *= scale_x
        boxes[:, [1, 3]] *= scale_y
        landmarks *= np.array([scale_x, scale_y])[None]

        return (boxes, confidence, landmarks)    


    def step(self, image):        
        x = self.preprocess(image)
        inputs = {self.session.get_inputs()[0].name: x}
        predictions = self.session.run(None, inputs)[0][0]
        (boxes, confidence, landmarks) = self.postprocess(predictions, input_resolution=image.shape[:-1], model_resolution=(640, 640))
        return (boxes, confidence, landmarks)


if __name__ == "__main__":
    img = cv2.imread('data/2.jpg')
    # Load model 
    model_name = 'yolov8n-face.pt'

    if False:
        model = YOLO(model_name)  #https://github.com/akanametov/yolo-face/releases/download/v0.0.0/yolov8n-face.pt
        model.export(format="onnx", opset=14, simplify=True, dynamic=False)
        from ultralytics import YOLO
        # Run inference    
        results = model(img)[0]  # process only the first image result
        for det in results.boxes.data.cpu().numpy():
            x1, y1, x2, y2, conf, cls = det[:6]
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            
            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Get landmarks
            # Landmarks are in results.keypoints
            if results.keypoints is not None:
                for kpt in results.keypoints.data.cpu().numpy():
                    for i in range(5):  # assuming 5 facial landmarks
                        x, y = kpt[i][:2]
                        cv2.circle(img, (int(x), int(y)), 3, (0, 255, 0), -1)

        # Show result
        cv2.imshow('YOLOv8-Face', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    fd = FaceDetector(model_name[:-2] + 'onnx')
    boxes, confidence, landmarks = fd.step(img)

    for det in boxes:
        x1, y1, x2, y2 = det
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        
        # Draw bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
        # Get landmarks
        # Landmarks are in results.keypoints
        if len(landmarks) > 0:
            for kpt in landmarks:
                for i in range(5):  # assuming 5 facial landmarks
                    x, y = kpt[i][:2]
                    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)


    # Show result
    cv2.imshow('YOLOv8-Face', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()