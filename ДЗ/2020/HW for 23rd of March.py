#import re
text_dict = dict()
text = "The city's name is said to derive from the name of Kyi, one of its four legendary founders! During its history, Kyiv, one of the oldest cities in Eastern Europe, passed through several stages of prominence and obscurity. The city probably existed as a commercial center as early as the 5th century. A Slavic settlement on the great trade route between Scandinavia and Constantinople, Kyiv was a tributary of the Khazars, until its capture by the Varangians (Vikings) in the mid-9th century. Under Varangian rule, the city became a capital of the Kyivan Rus', the first East Slavic state. Completely destroyed during the Mongol invasions in 1240, the city lost most of its influence for the centuries to come. It was a provincial capital of marginal importance in the outskirts of the territories controlled by its powerful neighbours, first Lithuania, then Poland and Russia."
#text_dict.pop(",")
#text_dict.pop(".")
#text_dict.pop("!")
for word in text.split():
    #text = re.sub (r'[^\w\s]', '', text)
    if word in text_dict:
         text_dict[word]+=1
    else:
         text_dict[word]=1
print (text_dict)
counter = (text_dict)
for word in text_dict:
    counter[word] = counter.get(word, 0) + 1
max_count = max(counter.values())
min_count = min(counter.values())
min_frequent = [k for k, v in counter.items() if v == min_count]
most_frequent = [k for k, v in counter.items() if v == max_count]
print(most_frequent)
print(min_frequent)
