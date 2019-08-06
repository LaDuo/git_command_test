import re


###########################################检测Stub是否丢包
# 输出行号
# with open("C:\\Users\\dulid\\Desktop\\Av2_Output\\outfile.txt", 'r') as f:
#     for (num, value) in enumerate(f):
#         print(num, value)

pattern = re.compile(r".+\*.+")
pattern_long1 = re.compile(".+Profile Long: type=1.+")
pattern_long2 = re.compile(".+Profile Long: type=2.+")
pattern_long3 = re.compile(".+Profile Long: type=9.+")
pattern_short1 = re.compile(".+Profile Short: type=1.+")
pattern_short4 = re.compile(".+Profile Short: type=4.+")
pattern_time = re.compile(r"\d+-\d+ \d+:\d+:\d+\.\d+")

list_long1 = []
long1_time = []
list_long2 = []
long2_time = []
list_long9 = []
long9_time = []
list_short1 = []
short1_time = []
list_short4 = []
short4_time = []
lists = []

with open("C:\\Users\\dulid\\Desktop\\Av2_Output\\outfile.txt", 'r', encoding='utf-8') as f:
    lists = f.readlines()
count = 0

for se in lists:
    count += 1
    length = len(se)
    times = pattern_time.findall(se)
    m = pattern_long1.findall(se)
    n = pattern_long2.findall(se)
    p = pattern_long3.findall(se)
    s = pattern_short1.findall(se)
    t = pattern_short4.findall(se)
    if m:
        list_long1.append(se[length - 2])
        long1_time.append(times)
    elif n:
        list_long2.append(se[length - 2])
        long2_time.append(times)
    elif p:
        list_long9.append(se[length - 2])
        long9_time.append(times)
    elif s:
        list_short1.append(se[length - 2])
        short1_time.append(times)
    elif t:
        list_short4.append(se[length - 2])
        short4_time.append(times)


def detect_long1():
    for index in range(len(list_long1) - 1):
        if list_long1[index] == "1":
            if list_long1[index + 1] == "2":
                continue
            else:
                print("error ---->  ", long1_time[index+1])
        if list_long1[index] == "2":
            if list_long1[index + 1] == "3":
                continue
            else:
                print("error ---->  ", long1_time[index+1])
        if list_long1[index] == "3":
            if list_long1[index + 1] == "0":
                continue
            else:
                print("error ----> ", long1_time[index+1])
        if list_long1[index] == "0":
            if list_long1[index + 1] == "1":
                continue
            else:
                print("error ---->  ", long1_time[index+1])


def detect_long2():
    for index in range(len(list_long2) - 1):
        if list_long2[index] == "1":
            if list_long2[index + 1] == "2":
                continue
            else:
                print("error ---->  ", long2_time[index+1])
        if list_long2[index] == "2":
            if list_long2[index + 1] == "3":
                continue
            else:
                print("error ---->  ", long2_time[index+1])
        if list_long2[index] == "3":
            if list_long2[index + 1] == "0":
                continue
            else:
                print("error ---->  ", long2_time[index+1])
        if list_long2[index] == "0":
            if list_long2[index + 1] == "1":
                continue
            else:
                print("error ---->  ", long2_time[index+1])


def detect_long9():
    for index in range(len(list_long9) - 1):
        if list_long9[index] == "1":
            if list_long9[index + 1] == "2":
                continue
            else:
                print("error ---->  ", long9_time[index+1])
        if list_long9[index] == "2":
            if list_long9[index + 1] == "3":
                continue
            else:
                print("error ---->  ", long9_time[index+1])
        if list_long9[index] == "3":
            if list_long9[index + 1] == "0":
                continue
            else:
                print("error ---->  ", long9_time[index+1])
        if list_long9[index] == "0":
            if list_long9[index + 1] == "1":
                continue
            else:
                print("error ---->  ", long9_time[index+1])


def detect_short1():
    for index in range(len(list_short1) - 1):
        if list_short1[index] == "1":
            if list_short1[index + 1] == "2":
                continue
            else:
                print("error ---->  ", short1_time[index+1])
        if list_short1[index] == "2":
            if list_short1[index + 1] == "3":
                continue
            else:
                print("error ---->  ", short1_time[index+1])
        if list_short1[index] == "3":
            if list_short1[index + 1] == "0":
                continue
            else:
                print("error ---->  ", short1_time[index+1])
        if list_short1[index] == "0":
            if list_short1[index + 1] == "1":
                continue
            else:
                print("error ---->  ", short1_time[index+1])


def detect_short4():
    for index in range(len(list_short4) - 1):
        if list_short4[index] == "1":
            if list_short4[index + 1] == "2":
                continue
            else:
                print("error ---->  ", short4_time[index+1])
        if list_short4[index] == "2":
            if list_short4[index + 1] == "3":
                continue
            else:
                print("error ---->  ", short4_time[index+1])
        if list_short4[index] == "3":
            if list_short4[index + 1] == "0":
                continue
            else:
                print("error ---->  ", short4_time[index+1])
        if list_short4[index] == "0":
            if list_short4[index + 1] == "1":
                continue
            else:
                print("error ---->  ", short4_time[index+1])


if __name__ == '__main__':
    detect_long1()
    detect_long2()
    detect_long9()
    detect_short1()
    detect_short4()
