#На вхід -- текст, на вихід:
#1) найдовше слово (слова)
#2) найкоротше слово (слова)
#3) найуживаніше слово (слова)
#4) частотний словник тексту
#5) словник слів тексту із кількістю голосних звуків у слові
#6) словник слів тексту із кількістю приголосних звуків у слові
word_list = input ("Введіть текст: ")
word_list = dict()
#x = word_list.split
def find_the_longest_word (word_list):
    the_longest = ''
    for word in word_list:
        if len (word) > len (the_longest):
            the_longest = word
            print (the_longest)
def find_the_shortest_word (word_list):
    the_shortest = ''
    for word in word_list:
        if len (word) < len (the_shortest):
            the_shortest = word
            print (the_shortest)

for word in word_list():
    if word in word_list:
         word_list[word] += 1
    else:
         word_list[word] = 1
new_dict = {key: str(round(value * 100 / sum(word_list.values()))) + "%" for key, value in word_list.items()}
print(new_dict)
