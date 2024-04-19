import logging
import os
import subprocess
import pygetwindow


def change_window(window_name):
    change_window_mac(window_name)


def change_window_mac(window_name):
    cmd = "open -a " + '\'' + window_name + '\''
    subprocess.call(cmd, shell=True)


def get_window_list():
    windows = []
    windows = get_window_list_mac()
    return windows


def get_window_list_mac():
    items = os.listdir('/Applications/')
    apps = [item for item in items if item.endswith('.app')]
    logging.debug(apps)
    return apps


