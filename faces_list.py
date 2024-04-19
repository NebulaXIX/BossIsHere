import logging
import os.path

import face_recognition

from file_utils import get_app_data_dir


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


def get_face_img_list(path=get_app_data_dir("BossFace")):
    logging.debug(f"{path}")
    if not check_path(path):
        raise Exception(f"未找到人脸库目录，请检查目录和权限！文件应当位于{path}")
    flag, faces = faces_list(path)
    if flag:
        raise Exception(f"未找到任何人脸数据，请确保人脸库中有数据且可读！当前人脸库{path}")
    return faces
