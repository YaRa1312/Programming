"""HW:length = ""
while not isinstance (length, int):
    try:
        length = int(input("Input length of the tuple. "))
    except:
        print("Please, try again. ")

list_tuple = []
for counter in range (length):
    while not isinstance (length, float):
        try:
            item = float (input ("Input length of the tuple. "))
        except:
            print ("Please, try again. ")
    list_tuple.append(item)

my_tuple = tuple(list_tuple)
del list_tuple

my_list=list(my_tuple)

def bubble_sort (list_to_sort):
    list_to_sort.sort(reverse=True)
    return list_to_sort

sorted_list = bubble_sort (my_list)

my_dict = dict()
counter = 0
for counter in range (length):
    my_dict[my_tuple[counter]] = sorted_list[counter]

my_2nd_dict = dict()
for item in my_tuple:
    my_2nd_dict[item] = sorted_list[counter]
    counter +=1

print(my_dict)
print(my_2nd_dict)
print(set (my_tuple))"""

my_list = [1, 5, 6, 2, 7, 10, 11, 9]
"""1) вибрати опорний елемент
будемо брати перший елемент.
2) порівняти всі елементи списку з опорним. Якщо елемент списку менший за опопрний
або дорівнює йому, то передаємо його у список 1, якщо більший -- у список 2.

o_el = 1
my_list = []
my_list
