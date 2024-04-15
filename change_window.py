import os
import subprocess
import pygetwindow


def change_window(window_name):
    if os.name == 'nt':
        change_window_win(window_name)
    else:
        change_window_mac(window_name)


def change_window_win(window_name):
    window = pygetwindow.getWindowsWithTitle(window_name)
    window.activateWindow()


def change_window_mac(window_name):
    cmd = "open -a " + '\'' + window_name + '\''
    subprocess.call(cmd, shell=True)


def get_window_list():
    windows = []
    if os.name == 'nt':
        windows = get_window_list_win()
    else:
        windows = get_window_list_mac()
    return windows


def get_window_list_win():
    return pygetwindow.getAllTitles()


def get_window_list_mac():
    items = os.listdir('/Applications/')
    apps = [item for item in items if item.endswith('.app')]
    print(apps)
    return apps


def window_exist(window_name):
    windows = get_window_list()
    return True
