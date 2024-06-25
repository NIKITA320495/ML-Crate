We're pioneering a novel solution leveraging YOLO deep learning techniques to address the urgent challenge of marine waste detection and management. Our system harnesses real-time object detection to swiftly and accurately identify diverse types of waste in marine environments.. Integrating with forward-looking sonar cameras on ships, our application receives real-time underwater images, serving as input for detection algorithms. Designed for scalability and adaptability across various ship types and marine settings, our web application utilizes cloud infrastructure to handle processing demands and accommodate the dynamic conditions encountered at sea.

best.pt is the trained AI model that detects the waste in the image. The model is trained on yolov8n

train and val folder contain dummy directory for trainig the model.

project.py has the flask code to connect our web interface with the the backend python model.

the frontend is done in files index.html and result.html
