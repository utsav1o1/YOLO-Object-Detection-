import cv2
from ultralytics import YOLO

model = YOLO('../Yolo-Weights/yolov8n.pt')
results = model("Images/3.jpg", show=True)

cv2.waitKey(0)