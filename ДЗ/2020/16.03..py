#my_dict = { "name": " Mariia",
   #         "surname": " Fedorova",
  #          "eyes": " brown",
 #           "hands": " hgkhk"
#}
#print(my_dict["eyes"])
#my_dict["eyes"] = "blue"
#print(my_dict.get("eyes"))

#for item in my_dict:
#    print(item)

#for item in my_dict:
#    print(my_dict[item])

#for item in my_dict.values():
 #   print(item)

#for key, value in my_dict.items():
 #   print (str(key) + ":" + str(value))
#print (my_dict["hgkhk"])

#if "hgkhk" in my_dict.values():
 #   print ("hgkhk in a key")
#else:
 #   print ("hgkhk is not in a key")
#print(len(my_dict))

#dict_list=[]
#for counter in range (len(my_dict)):
   # dict_list.append[counter]=str(counter)+("*th dict element is")
#print (dict_list)

#counter=0
#for key, value in my_dict.items():
 #   dict_list[counter]=[key, value]
#print(dict_list)

#my_dict["time"] = "10:00 - 11:00"
#print(my_dict)


#my_dict.pop("time")
#print(my_dict)

#my_dict.popitem()
#my_dict.popitem()

#del my_dict["eyes"]
#print(my_dict)

#del my_dict
#print (my_dict)

#my_dict2=dict(my_dict)
#print(my_dict2)

#my_dict.clear()
#print(my_dict)
#print(my_dict2)

#a=5
#b=a
#print(b)
#a=6
#print(b)

#x = 3

#my_dict2 = {
 #   "name": 12,
  #  "second": [1, 2, ["df", 5]],
   # "third": {"type": "C"},
   # 123: "try",
   # x: "variable value"
#}

#x=4

#print(my_dict2[3])

#my_dict=dict(name="Mariia", Surname = "Ivanova", year = 2020)
#print(my_dict)

#text_dict = dict()
#text = "the best the least the knu the knu best knu ever"
#for word in text.split():
    #print(word)
    #if word in text_dict:
   #     text_dict[word]+=1
  #  else:
 #       text_dict[word]=1
#print (text_dict)


#ДЗ: на вхід: довгий текст (з пробілами, комами, крапками тощо).
#На вихід: словник, у якого ключ - це слово з тексту, а значення ключа - частота, з якою це слово трапляється в тексті.
#Знайти слово, яке траплялося найчастіше і яке траплялося найменше.
#text = "Яриночко, допишеш цей код, і можна*спати."
#a = text.split()
#b = text.split("*")
#print(a, b)
#import re
#DATA = "Hey, you - what are you doing here!?"
#print re.findall(r"[\w']+", DATA)
#text_dict = dict('a;bcd,ef g')
 #   replace(';',' ').replace(',',' ').split()
#print (dict)
#import re
#text = 'The quick brown\nfox jumps*over the lazy dog.'
#print(re.split('; |, |\*|\n',text))
#asking = "". join (1 for 1 in asking if 1 not in (',', '.', '*'))
#print (asking)
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())
