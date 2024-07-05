# Real-Time Marine Object Detection Using Forward-Looking Sonar Cameras

## Overview
Our project centers on the development of a deep learning-based model tailored for real-time object detection using imagery from forward-looking sonar cameras installed on ships. This innovative application seeks to enhance maritime safety and environmental protection by identifying objects such as waste and obstructions in marine environments. 

Key to achieving this goal is the integration of advanced artificial intelligence (AI) techniques, specifically deep learning and computer vision, which enable accurate and efficient object detection in real-time.

## Introduction
### Leveraging Deep Learning and Computer Vision
Deep learning algorithms, particularly YOLO (You Only Look Once), have demonstrated exceptional capabilities in image recognition tasks. By leveraging these techniques, our system can analyze sonar images and accurately identify objects of interest, such as marine waste and potential hazards, with high precision and reliability. Computer vision algorithms further enhance the system's capabilities by enabling the extraction of relevant features from the sonar images, facilitating object recognition and classification.

### Real-Time Implementation
Real-time implementation is a critical aspect of our project, ensuring timely detection and response to potential threats in marine environments. Our system is designed to process sonar images in real-time, enabling swift detection of objects as they appear in the camera's field of view. This capability is essential for enhancing maritime safety by alerting ship operators to the presence of obstacles or hazardous materials in their vicinity, thereby enabling timely intervention to mitigate risks.

### Adaptability to Diverse Environmental Conditions
To ensure applicability across various water bodies, we have adopted a strategy of using only publicly available datasets for training and testing our AI models. This approach allows our application to operate effectively in a wide range of marine environments, from coastal regions to open seas. By training our models on diverse datasets, we ensure that they can accurately detect and classify objects in different water conditions, depths, and lighting conditions.

## Vision and Mission
Our project represents a pioneering effort in leveraging AI technologies for real-time object detection in marine environments. By combining advanced deep learning and computer vision techniques with real-time implementation and the use of public datasets, we provide a comprehensive solution for enhancing maritime safety and environmental protection. Our application holds great promise in addressing the pressing challenges of marine waste detection and mitigation, contributing to the preservation of marine ecosystems and the sustainable management of marine resources.

## Methodology
Our project architecture encompasses the development of a comprehensive website that embodies our vision and mission, showcasing the capabilities of our real-time marine object detection system. At the heart of this architecture is a seamless integration of front-end and back-end technologies, culminating in a user-friendly interface that allows visitors to interact with our model and witness its capabilities firsthand.

## Interface 
![interface](https://github.com/NIKITA320495/ML-Crate/blob/main/Marine-Waste-Detection/Images/interface.png)
## Machine Learning Model

In our marine object detection model, we conducted a thorough class analysis of the marine_debris_fls dataset, identifying 11 unique classes such as wall, can, tire, and bottle. We split the dataset into training (80%) and validation (20%) sets, creating a data_custom.yaml configuration file for the YOLO framework. Utilizing the yolo8n.pt pretrained model, we fine-tuned it on our custom dataset, resulting in the trained model best.pt. We developed predict.py to perform inference on images and videos, accurately identifying and localizing marine debris. This comprehensive pipeline effectively addresses marine debris detection in aquatic environments.

###Lables
![labels](https://github.com/NIKITA320495/ML-Crate/blob/main/Marine-Waste-Detection/Images/labels.jpg)
### Working 
![](https://github.com/NIKITA320495/ML-Crate/blob/main/Marine-Waste-Detection/Images/val_batch2_pred.jpg)
### Results
![](https://github.com/NIKITA320495/ML-Crate/blob/main/Marine-Waste-Detection/Images/working.png)
