my_tuple = ("set", "dict", "list")
#print(my_tuple)
#print(type(my_tuple))
#print(my_tuple[2])
#print(my_tuple[-2])
#print(my_tuple[0:2])
#print(my_tuple[-1:-3])
#print(type(my_tuple[-1:-3]))
#my_list = list(my_tuple)
#print(my_list)
#my_list[1] = "tuple"
#print(my_list)

#list_item = [3, "5"]
#list_to_change = ["we've changed this list"]
#my_tuple = ("set", "dict", "list", 4, list_item)
#for item in my_tuple:
#    print (item)

#number=7
#my_tuple = ("set", "dict", "list", 4, {1:2, "sdf": 4}, {"word", 6, "is"}, (1, 3, 5))
#print (my_tuple)
#number=8
#print(len(my_tuple))

#test_tuple = ("tuple", )
#print(test_tuple)
#print(type(test_tuple))
#del test_tuple
#print (test_tuple)

#first_tuple = (1, 2, 3, 4, 5)
#second_tuple = ("1st", "2nd", 5)
#join_tuple = first_tuple + second_tuple
#print (join_tuple)

#my_tuple = tuple((1, 3, "dgdfg"))
#print (my_tuple)

#print(join_tuple. count("2"))
#print(join_tuple.index(5))

...
#f(n) = n!
#f(n) = n*(n-1) and f(1) = 1
#f(n) n*f(n-1) and f(1) = 1
#...
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
print(f(5))

...
#f(a,b) = a*b
#(a,b) = a + f(a, b-1) if b>1
#(a, 1)=a
#...
def f (a, b):
    if b>1:
        return a + f(a, b-1)
    else:
        return a
print (f(5,6))

#f(n) = "a...a" n times
#f(n) = f(n-1) + f(1) if n>1
#f(n) = "a"
#...
#def f(n):
#    if n>1:
#        return f(n-1) + f(1)
#    else:
#        return "a"
#print (f(7))
#...
#ДЗ: створити кортеж із 7-м елементів, які вводить коритувач (-ка), - дійсних чисел. Створити список за цим кортежем.
#Відсортувати список на спадання, використовуючи бабл-сорт
#Створити словник, ключами якого будуть значення кортежу, а значеннями -- значення відсортованого
#Створити множину з кортежу.
#Приклад:
#(2.1, 4.0, 17, 8, 4.0) - tuple
#list: [2.1, 4.0, 17, 8, 4.0]
#sorted_list: [17, 8, 4.0, 4.0, 2.1]
#dict: {2.1:17,
#       4.0: 8,
#       17: 4.0,
#       8: 4.0,
#       4.0: 2.1
#}
#set: {2.1, 4.0, 17, 8}

#Створити рекурсивну функцію, яка на вхід отримує рядок та натуральне число n,
#а повертає цей рядок записаний (n+1) раз
#Приклад:
#f("as", 3) = asasas
