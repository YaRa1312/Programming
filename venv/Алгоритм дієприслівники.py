import pymorphy2
from pymorphy2 import analyzer
from pathlib import Path
#У Богданки окремий файл "verbs_function" з ф-ми
#from verbs_function import Verbs
import csv

#names = ['counter', 'verb', 'aspect', 'adverb_pres', 'adverb_past']
#with open('smykovska.csv', 'a', encoding = 'utf-8') as text:
#    writer = csv.writer(text, delimiter = ';')
#    writer.writerow(names)

#file = open('D:\ВИШ\СУМ\Морфемологія СУМ\smykovska.csv', encoding = 'utf-8', mode = 'a')
#file = input("Enter the path here (with \\\\ for Windows): ").strip(' ')
#for path in Path(file).iterdir():
#    if path.is_file:
#        current_file = open(path, "r", encoding="utf-8")
# text = csv.reader(file)
# verbs = []
# for line in text:
#     verbs.append(line[0])
# file.close()

#file = open('D:\ВИШ\СУМ\Морфемологія СУМ\smykovska.csv', encoding = 'utf-8', mode = 'a')

morph = pymorphy2.MorphAnalyzer()
#
# data = file.read().split('\n')
#print(lines_list)

#вилучає перший елемент у списку списків (назви стовпчиків)
#data = data[1:104]
#print(lines_list)

#new_list.pop()
#print(new_list)

#робить список списків
#data = [elem.strip().split(",") for elem in data]

#шматочок коду, який прибирає ост ел-т (пустий список у списку списків) (особливість документу Каті Смиковської)
#data.pop()

#print(len(lines_list))
#print(lines_list)

# for element in range(len(lines_list)):
#     print(lines_list[element[:3]])
#print(data)
# def characteristics(verbs, morp=pymorphy2.MorphAnalyzer(lang='uk')):
#     counter = 0
#
#     for element in range(len(lines_list)):
#         word = verbs[element][0]
#         counter += 1
#         verb = moph.parse(word)[0]
#
#         aspect = verb.tag.aspect
#         if aspect == 'perf':
#             aspect = 'D'
#         else:
#             if aspect == 'inpf':
#                 aspect = 'N'
#             else:
#                 aspect = 'None'
#             lines_list[element] = [str(counter), verb[0], aspect]
#         return lines_list


#типу, має обрізати 2 ост ел-ти у списках, які є ел-тами списку списків
# def characteristics_slicing(verbs):
#     for element in range(verbs):
#         verbs[element] = verbs[element][:3]
#     print(verbs)
#     return(verbs)

# #перетворює список списків на стовпчик ліній
#for inner_list in lines_list:
#    print(inner_list)

#for inner_list in lines_list:
#    for i in inner_list:
#        i[:4] + " " + i[4+1: ]
#print(inner_list)

#для роботи з елементом у списку, який є елементом списку списків,треба
#назва_загал_списку[номер списку, який є ел-том загал списку][номер ел-та у списку, що є ел-том загал списку]

file=open('D:\ВИШ\СУМ\Морфемологія СУМ\smykovska.csv','r', encoding = 'utf-8')
lines_list=file.read().split('\n')
lines_list.pop()
lines_list = lines_list[1:104]
morph=pymorphy2.MorphAnalyzer(lang='uk')
for counter in range(len(lines_list)):
    lines_list[counter]=lines_list[counter].split(';')
for line in lines_list:
       for counter in range(len(line)):
          line[counter]=line[counter].strip('')
       for el in range(len(line)):
           number_bool = False
           if line[4][-1:] == '1' or line[4][-1:] == '2':
               number_bool = True
               line[4] = line[4][:-1]
           text_bool = False
           if line[3][-1:] == 'P' or line[3][-1:] == 'E':
               text_bool = True
               line[3] = line[3][:-1]
           #mode_bool = False
           aspect = line[2][-1]
           if aspect == 'perf':
               aspect = 'D'
           elif aspect == 'impf':
               aspect = 'N'
           else:
               aspect = 'None'
           word = line[1][-1:]
           line = moph.parse(word)[1]
           #line[4].append("")





       # sia_bool=False
       # if line[1][-2:]=='ся'or line[1][-2:]=='сь':
       #     sia_bool=True
       #     line[1]=line[1][:-2]

print(lines_list)