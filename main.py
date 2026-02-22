import cv2
from ultralytics import YOLO

# Load a stronger model (more accurate than yolov8n)
model = YOLO("yolov8m.pt")  # m = medium (more accurate)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.6)  # Only show detections above 60%

    detected_objects = []  # <-- This is your variable

    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = model.names[class_id]

            # Bounding box coords
            x1, y1, x2, y2 = box.xyxy[0]

            detected_objects.append({
                "label": label,
                "confidence": confidence,
                "box": (int(x1), int(y1), int(x2), int(y2))
            })

    print(detected_objects)  # Now everything is stored in a variable

    annotated_frame = results[0].plot()
    cv2.imshow("AI Camera", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()