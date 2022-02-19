sub_list=['a',12,'bc']
sup_list=[1,11,'d']
sup_list.extend(sub_list)
print (sup_list)
sup_list[4]*=2
print (sup_list)
sup_list.insert(4, 12)
print(sup_list)
counter_list=[ ]
for counter in range (len(sup_list)):
    counter_list.insert(0, sup_list[int(counter)])
    reversed(counter_list)
print(counter_list)
