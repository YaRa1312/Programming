print("Плешивцева Ірина, Прикладна лінгвістика, Лабораторна робота №1")
line = input("Введіть текстовий рядок: ")
#Ми наробили кіборгів у підземному бункері.
print(line)
z = line[:9]
res_a = z[3:]
print("Завдання 2(а):", res_a)
y = line[3:4]
x = line[4:5]
w = line[6:7]
res_b = "Завдання 2(б): " + y + ", " + x + ", " + w
print(res_b)
for i in line:
    for el in "аоуиіеяюєїАОУИІЕЯЮЄЇ":
        line = line.replace(el, "")
print("Завдання 2(в):", line)
import re
l = input("Введіть текстовий рядок українською мовою: ")
#Гей, хлопці, не вспію - на ґанку ваша файна їжа знищується бурундучком.
#Зараз спробую захистити її, але бурундучок сильний, а я одна, тому
#поспішайте, будь ласка.
replaces = {"А": "A", "Б": "B", "В": "W", "Г": "H", "Ґ": "G", "Д": "D", "Е": "E",
            "Є": "Je", "Ж": "Ż", "З": "Z", "И": "Y", "І": "I", "Ї": "Ji", "Й": "J",
            "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R",
            "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "Ch", "Ц": "C", "Ч": "Cz",
            "Ш": "Sz", "Щ": "Szcz", "Ь": "", "Ю": "Ju", "Я": "Ja",
            "а": "a", "б": "b", "в": "w", "г": "h", "ґ": "g", "д": "d", "е": "e",
            "є": "je", "ж": "ż", "з": "z", "и": "y", "і": "i", "ї": "ji", "й": "j",
            "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
            "с": "s", "т": "t", "у": "u", "ф": "f", "х": "ch", "ц": "c", "ч": "cz",
            "ш": "sz", "щ": "szcz", "ь": "", "ю": "ju", "я": "ja"}
regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], l)
print("Завдання 3: ", regex)

#код із заняття 6 жовтня (про ворднет)
#from nltk.corpus import wordnet as wn
#for synset in wn.synset('java', wn.NOUN):
#    print(synset.name() + ":", synset.definition())
#for synset in wn.synset('java'):
#    print(synset.lemma_names())