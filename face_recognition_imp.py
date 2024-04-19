import cv2
import face_recognition

from faces_list import get_face_img_list
from file_utils import get_app_data_dir

encodings = []


def load_faces(path=get_app_data_dir("BossFace"), **args):
    faces_img = get_face_img_list(path)
    for face_img in faces_img:
        img = cv2.imread(face_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_encodings = face_recognition.face_encodings(img, model=args['model'])
        for encoding in img_encodings:
            encodings.append(encoding)


def recognize_faces(img, args):
    cv2.resize(img, (256, 256))
    faces_encoding = face_recognition.face_encodings(img, model=args['model'])
    result = []
    if len(faces_encoding):
        for face_encoding in faces_encoding:
            matches = face_recognition.compare_faces(encodings, face_encoding, tolerance=args['tolerance'])
            for match in matches:
                result.append(match)
        if True in result:
            return True
        else:
            return False
    return False
