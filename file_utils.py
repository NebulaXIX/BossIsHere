import logging
import os


def home_dir():
    path = os.path.expanduser("~")
    return path


def exist_app_data_dir(dir_name):
    path = os.path.join(get_app_data(), dir_name)
    return os.path.exists(path)


def get_app_data():
    path = os.path.join(home_dir(), "Library/BossIsHere")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_app_data_dir(dir_name):
    path = os.path.join(get_app_data(), dir_name)
    return path


def create_app_data_dir(dir_name):
    if not exist_app_data_dir(dir_name):
        os.makedirs(get_app_data_dir(dir_name))


def crate_app_data():
    if not os.path.exists(get_app_data()):
        os.makedirs(get_app_data())
