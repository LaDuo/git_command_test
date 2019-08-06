import re

lists = []

pattern1 = re.compile(r'Position: path=12')
pattern2 = re.compile(r'Position: path=11')
pattern3 = re.compile(r'Position: path=10')
pattern_time = re.compile(r"\d+-\d+ \d+:\d+:\d+\.\d+")

with open('C:\\Users\\dulid\\Desktop\\Av2_Output\\outfile.txt', 'r', encoding='utf-8') as f:
    lists = f.readlines()


with open('C:\\Users\\dulid\\Desktop\\Av2_Output\\a.txt', 'w') as f1:
    for i in range(len(lists)):
        m = pattern1.findall(lists[i])
        n = pattern2.findall(lists[i])
        s = pattern3.findall(lists[i])

        if m:
            time = pattern_time.findall(lists[i])
            f1.write(str(time))
            f1.write("Position: path=12")
            f1.write('\n')
        elif n:
            time = pattern_time.findall(lists[i])
            f1.write(str(time))
            f1.write("Position: path=11")
            f1.write('\n')
        elif s:
            time = pattern_time.findall(lists[i])
            f1.write(str(time))
            f1.write("Position: path=10")
            f1.write('\n')



# for i in range(len(lists)):
#     m = pattern.findall(lists[i])
#     if m:
#         with open('C:\\Users\\dulid\\Desktop\\Av2_Output\\a.txt', 'w', encoding='utf-8') as f:
#             f.write(str(m) + lists[i][47] + lists[i][48])


# for i in range(len(lists)):
#     if i == (len(lists) - 1):
#         break
#     # print(lists[i])
#     m = pattern.findall(lists[i])
#     if m:
#         s = i
#         print(" m  -  i = ", i)
#         flag = 0
#         while(m):
#             if i == len(lists) - 1:
#                 break
#             i += 1
#             n = pattern.findall(lists[i])
#             if n:
#                 if lists[i][48] != lists[s][48] or lists[i][47] != lists[s][47]:
#                     # print("error --->", pattern_time.findall(lists[i]))
#                     flag = 1
#             if flag:
#                 break