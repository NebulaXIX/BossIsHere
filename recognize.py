import cv2
import face_recognition


def recognize_img(img, encodings):
    img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(img)
    matches = face_recognition.compare_faces(encoding, encodings)
    if True in matches:
        return True
    else:
        return False
