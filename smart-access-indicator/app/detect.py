from ultralytics import YOLO

VEHICLE_CLASSES = [2, 3, 5, 7, 16]


class VehicleDetector:
    def __init__(self,
                 model_path='models/yolov8n.pt',
                 imgsz=640,
                 conf=0.15):               
        self.model = YOLO(model_path)
        self.imgsz = imgsz
        self.conf  = conf                

    def detect(self, frame):
        r = self.model(frame,
                       imgsz=self.imgsz,
                       conf=self.conf,      
                       classes=VEHICLE_CLASSES)
        return r[0].boxes

