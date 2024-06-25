from ultralytics import YOLO
import numpy

# load a pretrained YOLOv8n model
model = YOLO('best.pt')  


detection_output = model.predict(source="converted-video (8).mp4", save=True) 


print(detection_output)


# print(detection_output[0].numpy())


# from ultralytics import YOLO
# import cv2

# # Load the pre-trained YOLOv model
# model = YOLO("best.pt")

# # Open the input video file
# input_video_path = "input_video.mp4"
# cap = cv2.VideoCapture(input_video_path)

# # Get the video properties (e.g., frame width, height, FPS)
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))

# # Define the codec and create VideoWriter object
# output_video_path = "output_video.mp4"
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# # Process each frame in the input video
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break  # Break the loop if no more frames are available

#     # Perform object detection on the current frame
#     results = model(frame)

#     # Draw bounding boxes on the frame
#     for box in results.xyxy[0]:
#         x_min, y_min, x_max, y_max, conf, class_id = box.tolist()
#         if conf > 0.5:  # Filter out low-confidence detections
#             cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
#             cv2.putText(frame, f"{model.names[int(class_id)]} {conf:.2f}", (int(x_min), int(y_min - 10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Write the annotated frame to the output video file
#     out.write(frame)

# # Release the video capture and writer objects
# cap.release()
# out.release()
