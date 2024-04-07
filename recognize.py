import importlib

import cv2


def recognize_img_imp(img, args):
    if args.get('imp') is None:
        module = importlib.import_module('face_recognition_imp')
    model = importlib.import_module(args['imp'])
    return model.recognize(img)


def recognize_img(img, **args):
    return recognize_img_imp(img, args)
