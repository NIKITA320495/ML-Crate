from ultralytics import YOLO
import numpy

directory = "results"
# load a pretrained YOLOv8n model
model = YOLO('best.pt')  


detection_output = model.predict(source="test.png", save=True, save_dir = directory) 


print(detection_output)


# print(detection_output[0].numpy())