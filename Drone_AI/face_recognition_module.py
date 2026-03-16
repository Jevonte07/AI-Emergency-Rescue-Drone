import face_recognition
import cv2

known_encoding = None


def load_known_face():

    global known_encoding

    image = face_recognition.load_image_file("drone_ai/known_faces/victim.jpg")
    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        known_encoding = encodings[0]
        print("Victim face loaded")
    else:
        print("No face found in victim image")


def identify_from_camera():

    video = cv2.VideoCapture(0)

    ret, frame = video.read()

    if not ret:
        return False

    rgb = frame[:, :, ::-1]

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding in encodings:

        matches = face_recognition.compare_faces([known_encoding], encoding)

        if True in matches:
            print("Victim identified")
            video.release()
            return True

    video.release()
    return False