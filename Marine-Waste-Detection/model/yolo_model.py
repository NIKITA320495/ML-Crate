from ultralytics import YOLO
import yaml
import numpy

# load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")  

# with open("data_custom.yaml") as f:
#     data = yaml.safe_load(f)



model.train(data = "E:\marine\data_custom.yaml",epochs=5)

# predict on an image
# detection_output = model.predict(source="try1.jpeg", conf=0.25, save=True) 

# # Display tensor array
# print(detection_output)

# # Display numpy array
# print(detection_output[0].numpy())


# Load the YAML file


# Assign the file object to the `yaml_file` key

