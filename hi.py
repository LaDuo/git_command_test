import re
import os
import shutil

def move():
    # Move the data to the another folder
    alllist =os.listdir(u"D:\\BaiduNetdiskDownload\\format\\")
    for i in alllist:
        aa,bb = i.split(".")
        if "_Av2数据" in aa:
            oldname = u"D:\\BaiduNetdiskDownload\\format\\" + aa + "." + bb
            newname = u"C:\\Users\\z1339\\Desktop\\input\\" + aa + "." + bb
            shutil.copyfile(oldname,newname)


def delete():
    # Delete the data which is unuseful
    alllist = os.listdir(u"D:\\BaiduNetdiskDownload\\format\\")
    base_path = "D:\\BaiduNetdiskDownload\\format\\"

    for j in alllist:
        if ".txt" in j:
            path = os.path.join(base_path,j)
            os.remove(path)






