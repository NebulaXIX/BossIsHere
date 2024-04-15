import importlib


def recognize_img_imp(img, args):
    if args.get('imp') is None:
        module = importlib.import_module('face_recognition_imp')
    else:
        module = importlib.import_module(args['imp'])
    return module.recognize(img)


def recognize_img(img, **args):
    return recognize_img_imp(img, args)
