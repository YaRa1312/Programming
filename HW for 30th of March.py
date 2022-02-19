text_dict = dict()
text = "hello world hello my love"
for word in text.split():
#    print(word)
    if word in text_dict:
         text_dict[word] += 1
    else:
         text_dict[word] = 1
print (text_dict)
#for word in text.split():
#    print(word)
#    text_dict[word] = text.count(word)
#print (text_dict)
#new_dict = {key: str(round(value * 100 / sum(text_dict.values()))) + "%" for key, value in text_dict.items()}
#print(new_dict)
