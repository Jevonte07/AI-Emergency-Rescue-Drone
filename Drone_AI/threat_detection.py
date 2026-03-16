import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_threat():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        for r in results:
            boxes = r.boxes

            for box in boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                label = model.names[cls]

                if label in ["knife", "gun", "person"]:

                    cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,255),2)
                    cv2.putText(frame,f"Threat: {label}",
                                (x1,y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7,(0,0,255),2)

        cv2.imshow("Threat Detection",frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()