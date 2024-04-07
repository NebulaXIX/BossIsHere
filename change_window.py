import webbrowser


def change_window(window_name):
    url = 'https://learn.microsoft.com/zh-cn/dotnet/api/system.datetime?view=net-8.0&redirectedfrom=MSDN'
    webbrowser.open(url)


def window_exist(window_name):
    return True


def create_window(window_name):
    return None
