import re

file = open('D:\ВИШ\КУРСОВА\Пробні текстові файли\Текст 1.csv','r', encoding = 'utf-8')

lines_list = file.read().split('\n')
lines_list.pop()
#друк одного з рядків файлу (у квадратних дужках індекс, послідовність індексів починається з 0)
print(lines_list[6])

latin_words = re.compile(r"")

file.close()
