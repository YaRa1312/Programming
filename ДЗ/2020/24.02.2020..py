list_of_num=[1, 5, 4.5, 7]
print(list_of_num)
print(type(list_of_num))
empty_list=[ ]
print(empty_list)
print(type(empty_list))
list_of_let=list("список")
print(list_of_let)
print(list_of_let[2])
list_of_tr=[let*3 for let in list_of_let]
print (list_of_tr)
dif_list=[1, "c", [2, 3], [2, "ca"]]
print(dif_list)
list_of_tr=[let*3 for let in dif_list]
print (list_of_tr)
dif_list_2=[counter*2 for counter in dif_list]
print(dif_list_2)
for counter in range(15):
    print (counter)
list_mult3=[3*counter+3 for counter in range (15)]
print(list_mult3)
list_mult3_v1=[3*counter for counter in range (1, 16)]
print(list_mult3_v1)
list_mult3_v2=[counter for counter in range (3, 46, 3)]
print(list_mult3_v2)
for counter in range (3, 46, 3):
    list_mult3_v3.append(counter)
list_mult3_v3=list()
print (list_mult3_v3)
for counter in range (3, 46, 3):
    list_mult3_v3.append(counter)
print(list_mult3_v3)
