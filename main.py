import importlib
import os.path
import threading
import time
from time import sleep
import logging
import face_recognition_imp
from camera_source import get_camera_list, get_pic_from_camera
from change_window import change_window
from file_utils import crate_app_data

flag = False
lock = threading.Lock()
module = None


def change_window_job(window):
    global flag
    while True:
        time.sleep(0.5)
        if flag:
            change_window(window)
            time.sleep(300)
            with lock:
                flag = False


def single_camera_job(cap, **args):
    global flag
    global module
    while True:
        time.sleep(0.5)
        img = get_pic_from_camera(cap)
        if module.recognize_faces(img, args):
            with lock:
                flag = True
            sleep(300)


def get_recognition_imp(imp=None):
    global module
    try:
        module = importlib.import_module(imp)
    except Exception:
        module = face_recognition_imp


def log_init():
    crate_app_data()
    path = os.path.join(os.path.expanduser("~"), "Library/BossIsHere/logs")
    if not os.path.exists(path):
        os.mkdir(os.path.join(os.path.expanduser("~"), "Library/BossIsHere/logs"))
    logging.basicConfig(filename=os.path.join(os.path.expanduser("~"), "Library/BossIsHere/logs/BossIsHere.log"),
                        filemode='w+', level=logging.DEBUG)


if __name__ == '__main__':
    window_name = "wpsoffice"
    log_init()
    try:
        cameras = get_camera_list()
        get_recognition_imp()
        args = {"tolerance": 0.4, "model": "large"}
        module.load_faces(tolerance=args["tolerance"], model=args["model"])
        for camera in cameras:
            threading.Thread(target=single_camera_job, args=(camera,), kwargs=args,
                             name='camera-' + camera.getBackendName()).start()
        threading.Thread(target=change_window_job, args=(window_name,), name='change_window').start()
        while True:
            time.sleep(10000)
    except Exception as e:
        logging.debug(f"{e}")
