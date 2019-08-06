import zipfile,os



def FileToZip1(filepath):
    zip_name = filepath + '.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(filepath):
        fpath = dirpath.replace(filepath, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            print("Success")
    z.close()






if __name__ == '__main__':
    path1 = "D:\\BaiduNetdiskDownload\\format"
    path2 = ""
    path3 = ""
    path4 = ""
    
    FileToZip1(path1)


