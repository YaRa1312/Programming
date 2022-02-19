import re
# #(([1-2]\d|0[1-9])\-(0[1-9]|1[012])|30\-(0[13-9]|1[0-2])|31\-(0[13578]|1[02]))\-\d{4} [^0]\d{3}-\0[^2]|1[1-2]
file = open('D:\ВИШ\Programming\exam.txt', 'r')
for line in file:
    res1 = re.findall('[^0]\d{3}-', line)
    print(res1[0])
    res2 = re.findall('-[1-2]\d|0[1-9]-', line)
    print(res2[0])
    print(res2[1])
    res2[0] = res2[0][1:3]
    print(res2[0])
    res2[1] = res2[1][1:3]
    print(res2[1])
    res1[0] = res1[0][2:4]
    print(res1[0])
    print(res2[1] + '.' + res2[0] + '.' + res1[0] + '.')
    #dayandmonth = re.findall('')