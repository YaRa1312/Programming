import pymorphy2
from pymorphy2 import analyzer
import csv
#import copy

morph = pymorphy2.MorphAnalyzer(lang='uk')

file=open('D:\ВИШ\СУМ\Морфемологія СУМ\smykovska.csv','r', encoding = 'utf-8')
lines_list = file.read().split('\n')
lines_list.pop()
lines_list = lines_list[1:104]
#print(lines_list[1])
for counter in range(len(lines_list)):
    lines_list[counter] = lines_list[counter].split(';')
for i in range(len(lines_list)):
    #print(lines_list[i][1]) #початкове слово
    butyavka1 = morph.parse(lines_list[i][1])[0]#відмінювання
    #print(butyavka1.tag.POS)
    try:
        present = butyavka1.inflect({'plur', '3per', 'pres'})[0] #бажана словоформа
        print(present)
    except TypeError:
        print(" ")
    if present[-2:] == 'ся':
       present = present[:-4]
       print(present + 'чись')
    else:
       present = present[:-2]
       print(present + 'чи')
    past = lines_list[i][1]
    if past[-2:] == 'ся':
       past = past[:-4]
       print(past + 'вшись')
    else:
       past = past[:-2]
       print(past + 'вши')
    # butyavka2 = morph.parse(lines_list[i][1])[0]
    # try:
    #    present = butyavka2.inflect({'sing', '3per', 'masc', 'past'})[0] #бажана словоформа
    #    print(present)
    # except TypeError:
    #    print(" ")
    # if present[-2:] == 'ся':
    #    present = present[:-2]
    #    print(present + 'шись')
    # else:
    #    #past = past[:-2]
    #    print(present + 'ши')

    # person = butyavka.inflect({'plur', '3per', 'pres'})[0]
    # print(type(butyavka))
    # res = list(butyavka)
    # return res  17.inflect({'plur', '3per', 'pres'})[0]
    #print(person)
    #print("Elements: ", res)
    #потрібно дістати із бутявки об'єкт під назвою word, щоб працювати саме з ним
    # if lines_list[i][1] != None:
    #     try:
    #         if butyavka[0][-2:] == 'ся':
    #            butyavka[0] = butyavka[0][:-4]
    #            print(butyavka[0] + 'чись')
    #         else:
    #            butyavka[0] = butyavka[0][:-2]
    #            print(butyavka[0] + 'чи')
    #     except TypeError:
    #          print("Oops!")


#butyavka.inflect({'plur', '3per'})
  #  butyavka = morph.parse.inflect((lines_list[i][1])({'plur', '3per'}))
    #butyavka.inflect({'plur', '3per'})[0] #відмінювання
  #  butyavka.tag.aspect
 #   print(butyavka.tag.aspect) #після аналізу
    #if butyavka.tag.aspect == 'perf':
        #print(butyavka.word)

   # print(morph.parse(lines_list[2][1])[0].inflect({'sing', 'nomn'}))
       # for counter in range(len(line)):
       #    line[counter] = line[counter].strip('')
       #    #print(line[1]) # стовчик слів
       #    adv_pres = line[1]

         # adv_pres = morph.parse(line[1])[0].inflect({'sing', 'nomn'}).word
         # print(adv_pres)
            #print((line[1]))
       #for el in range(len(line)):
           # number_bool = False
           # if line[4][-1:] == '1' or line[4][-1:] == '2':
           #     number_bool = True
           #     line[4] = line[4][:-1]
           #     print(line[4])
           # text_bool = False
           # if line[3][-1:] == 'P' or line[3][-1:] == 'E':
           #     text_bool = True
           #     line[3] = line[3][:-1]
           # aspect = line[2][-1:]
           # if aspect == 'perf':
           #     aspect = 'D'
           # elif aspect == 'impf':
           #     aspect = 'N'
           # else:
           #     aspect = 'None'
           #verb = line[1]
           #verb = morph.parse(verb)
           #line[1] = verb.inflect({'plur', '3per'})[0]
           #verb = copy.copy(verb)
           #line.append(verb)
           #початкова форма слова
           #start =
           #adv_pres = morph.parse(verb)[0].inflect({'sing', 'nomn'}).word
           #print(adv_pres)
           #закінчення
           # adv_pres = verb
           # if aspect == 'N':
           #     try:
           #         verb = verb.inflect({'plur', '3per'})
           #     except TypeError:
           #         line.append(None)
               #     continue
               # if line[1][-2:] == 'ся':
               #     line[1] = line[1][:-2]
               #     adv_pres = line[:-2] + 'чись'
               # else:
               #     adv_pres = line[:-2] + 'чи'
               # postfix = False
               # if verb[-2:] == 'ся' or verb[-2:] == 'сь':
               #     postfix = True
               # else:
               #     aspect = verb.tag.aspect

           #line.append(adv_pres)

           #adv_mod_perf += готовий дієприслівник
           #line[1] = moph.parse(word)[1]

#print(lines_list)