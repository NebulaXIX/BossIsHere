import cv2


def get_pic_from_camera(cap):
    ret, frame = cap.read()
    if not ret:
        raise Exception("摄像头读取失败！")
    return frame


def get_camera_list(num=5):
    cameras = []
    for i in range(num):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cameras.append(cap)
    return cameras
