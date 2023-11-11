# file = open('input.txt', 'a')
# print(file.read(4))
# print(file.tell())
# file.seek(1)
# print(file.tell())
# print(file.read())
#
# out_f = open('output.txt', 'rb')
# print(out_f.read())
# file = open('input.txt', 'r+')
# print(file.tell())
# file.write("12345")
# file.seek(0)
# print(file.read())
# print(file.tell())
#
# file.close()
#
# print(file.read())

# for line in file:
#     print(line)

# print(file.readlines())
# print(file.readline(5))
# print(file.tell())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.tell())

# with open('input.txt') as file:
#     for line in file:
#         print(line)

# with open('input.txt') as file:
#     text = file.readlines()
#
# list_text = []
# for item in text:
#     list_text.append(item.split()[0])
#
# print(list_text)
# print(text)

# list_text = []
# with open('input.txt') as file:
#     for line in file:
#          list_text.append(line)
# print(list_text)

list_text = []
with open('input.txt') as file:
    for line in file:
        list_text.append(file.readline())
print(list_text)

Input file: My name is. I study at.
User_name: Mariia
User_univ: KNU
Output: My name is Mariia. I study at KNU.
import re

text = """h<p>xfghfj<Name>MariiajMh,bh
</Name>
wiki (/ˈwɪki/ (About this soundlisten) WIK-ee) is a hypertext publication collaboratively Mariia edited and managed by its own audience directly using a web browser. A typical wiki contains multiple pages fojMariia<Name>r the subjecMariiats or scope of the project and may be either open to the public or limited <Name>Mto use within an organiz<Name>ation for maintaining its internal knowledge base.
</p>
<mariia@mail.ru khkjh
<mariia@ya.ru> kj
mari<p>ia@gmail.coma> kjkjn
mariia@gmail.com kjkjn
My name names is <name>. 
"""

#print(text)

# my_search = re.search('<p>', text)

# if my_search:
#   #  print(my_search.group())
#     #print(text[my_search.start():my_search.end()])
#     print(my_search.start())
#     print(my_search.end())
#     my_search_pos = my_search.span()
#     print(my_search_pos)
#     print(my_search_pos)
#     print(my_search_pos[0])
#     print(my_search_pos[1])
# else:
#     print("did not find")

# pattern = '(.+@(?!mail.ru|ya.ru)([a-zA-Z.]+))'
# my_match = re.match(pattern, text)
# #
# if my_match:
#      print(my_match.group(2))
# else:
#      print("did not find")

# my_findall = re.findall(pattern, text)
# print(my_findall)
#
# email_list = []
# for item in my_findall:
#     email_list.append(item[0])
# print(email_list)
#
# for counter in range(len(my_findall)):
#     my_findall[counter] = my_findall[counter][0]
# print(my_findall)

# word = "email"
# my_sub = re.sub(pattern, word, text)
# print(my_sub)
# print("text:")
# print(text)

# word = "email"
# my_sub = pattern.sub(word, text)
# print(my_sub)
# print("text:")
# print(text)
#
# my_split = re.split('[, .()<>\n/]', text)
# print(my_split)
pattern = r'\bname\b'
print(re.findall(pattern, text))
