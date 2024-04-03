import os.path
import re

import cv2


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return os.path.exists(path)


def faces_list(path):
    faces = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item):
            for img in os.listdir(item):
                faces.append(os.path.join(item_path, img))
        else:
            faces.append(item_path)
    if len(faces):
        return False, faces
    else:
        return True, faces


def get_face_list(path="./BossFace"):
    if not check_path(path):
        raise Exception("未找到人脸库目录，应当位于./BossFace，请检查目录和权限！")
    flag, faces = faces_list(path)
    if flag:
        raise Exception("未找到任何人脸数据，请确保人脸库中有数据且可读！")
    return faces
