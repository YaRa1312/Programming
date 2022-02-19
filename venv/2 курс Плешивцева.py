text_dict = dict()
text = """Fairies today are the stuff of children's stories , little magical people with wings , often shining with light .
Typically pretty and female , like Tinkerbell in Peter Pan , they usually use their magic to do small things and are mostly
friendly to humans .\n
We owe many of our modern ideas about fairies to Shakespeare and stories from the 18th and 19th centuries . Although we can 
see the origins of fairies as far back as the Ancient Greeks , we can see similar creatures in many cultures . The earliest 
fairy - like creatures can be found in the Greek idea that trees and rivers had spirits called dryads and nymphs . Some people
think these creatures were originally the gods of earlier , pagan religions that worshipped nature . They were replaced by the
Greek and Roman gods , and then later by the Christian God , and became smaller , less powerful figures as they lost importance .\n
Another explanation suggests the origin of fairies is a memory of real people , not spirits . So , for example , when tribes with 
metal weapons invaded land where people only used stone weapons , some of the people escaped and hid in forests and caves . 
Further support for this idea is that fairies were thought to be afraid of iron and could not touch it . Living outside of 
society , the hiding people probably stole food and attacked villages . This might explain why fairies were often described as 
playing tricks on humans . Hundreds of years ago , people actually believed that fairies stole new babies and replaced them 
with a changeling – a fairy baby – or that they took new mothers and made them feed fairy babies with their milk ."""
text_lower = text.lower()
print(text_lower)
#4) частотний словник
for word in text_lower.split():
    if word in text_dict:
         text_dict[word] += 1
    else:
         text_dict[word] = 1
#print (text_dict)

text_dict.pop('18th')
text_dict.pop('19th')
text_dict.pop(',')
text_dict.pop('.')
text_dict.pop('-')
text_dict.pop('–')

print(text_dict)
#1) найдовше слово (слова)
#2) найкоротше слово (слова)
sorted_list = sorted(text_dict.keys())

the_longest_word = []
the_longest_length = -1
the_shortest_word = []
the_shortest_length = float("Inf")
for word in sorted_list:
    if len (word) == the_shortest_length:
        the_shortest_word.append (word)
    if len (word) < the_shortest_length:
        the_shortest_length = len(word)
        the_shortest_word = [word]
    if len (word) == the_longest_length:
        the_longest_word.append (word)
    if len (word) > the_longest_length:
        the_longest_length = len (word)
        the_longest_word = [word]

print (the_longest_word)
print (the_shortest_word)

#3) найуживаніше слово (слова)
the_most_used_words = [word for max in [max(text_dict.values())] for word, counter in text_dict.items() if counter == max]
print (the_most_used_words)

#5) словник слів тексту із кількістю голосних звуків у слові
vowel_dict = {}
for word in sorted_list:
    counter = 0
    for vowel in "aoueyi":
        counter += word.count(vowel)
    vowel_dict.update({word: counter})
print (vowel_dict)

#6) словник слів тексту із кількістю приголосних звуків у слові
consonant_dict = {}
for word in sorted_list:
    counter = 0
    for consonant in "bcdfghjklmnpqrstvwxz":
        counter += word.count(consonant)
    consonant_dict.update({word: counter})
print (consonant_dict)
