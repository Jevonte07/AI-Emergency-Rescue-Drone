import cv2


def track_victim():

    cap = cv2.VideoCapture(0)

    tracker = cv2.TrackerCSRT_create()

    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        return

    bbox = cv2.selectROI(frame, False)

    tracker.init(frame, bbox)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        success, box = tracker.update(frame)

        if success:

            x, y, w, h = [int(v) for v in box]

            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

            cv2.putText(frame, "Tracking Victim",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

        cv2.imshow("Drone Camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()