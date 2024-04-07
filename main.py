import importlib
import threading
import time
from time import sleep

import face_recognition_imp
from camera_source import get_camera_list, get_pic_from_camera
from change_window import window_exist, create_window, change_window

flag = False
lock = threading.Lock()
module = face_recognition_imp


def change_window_job(window):
    global flag
    while True:
        time.sleep(0.1)
        if flag:
            change_window(window)
            time.sleep(300)
            with lock:
                flag = False


def single_camera_job(cap, **args):
    global flag
    global module
    while True:
        time.sleep(0.2)
        img = get_pic_from_camera(cap)
        if module.recognize_faces(img, args):
            with lock:
                flag = True
            sleep(300)


def get_recognition_imp(imp):
    global module
    try:
        module = importlib.import_module(imp)
    except:
        module = face_recognition_imp


if __name__ == '__main__':

    window_name = "Face Recognition"
    if not window_exist(window_name):
        create_window(window_name)
    cameras = get_camera_list()
    get_recognition_imp(None)
    args = {"tolerance": 0.8, "model": "large"}
    module.load_faces(tolerance=args["tolerance"], model=args["model"])
    for camera in cameras:
        threading.Thread(target=single_camera_job, args=(camera,), kwargs=args,
                         name='camera-' + camera.getBackendName()).start()
    threading.Thread(target=change_window_job, args=(window_name,), name='change_window').start()
    while True:
        time.sleep(10000)
