import os
from datetime import datetime

def get_path_desktop():
    return os.path.join(os.path.expanduser('~'), "Desktop")

def create_folder(path):
    base_path = path + "\\Analyze"
    if not os.path.exists(base_path):
        os.mkdir(base_path)
        print("创建成功")
        return True
    else:
        print("目录已存在")
        return False

def create_son_folder(path):
    basic_path = path + "\\Analyze"
    str = basic_path + datetime.now().strftime("%Y%m%d_%H%M%S")
    while True == os.path.exists(str):
        str = str + datetime.now().strftime("%Y%m%d_%H%M%S")

    os.makedirs(str)






if __name__ == '__main__':
    path = get_path_desktop()
    create_folder(path)

    create_son_folder(path)