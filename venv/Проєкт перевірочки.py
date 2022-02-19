import operator
from operator import itemgetter

f1 = open("D:\\ВИШ\\3 курс\\1-ий семестр\\ТПОПЛГ\\chesterton-thursday.txt", "r")
word_dict = dict()
f1.close()

with open("D:\\ВИШ\\3 курс\\1-ий семестр\\ТПОПЛГ\\chesterton-thursday.txt", 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            for el in '.,"-?!;:[]':
                word = word.replace(el, "")
            # print(word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    print(word_dict)

    sorted_word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))
    with open("highscore.txt", 'w') as f:
        for key, value in sorted_word_dict.items():
            f.write('%s\n' % (key))
        f.close()