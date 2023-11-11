my_list = [2, 5, 1, 6, 8, 27, 45, 192, 9]
#print(my_list)

def list_sort (sorted_list):
    big_cycle_cont = True
    list_length = len(sorted_list)
    big_counter = 0
    while big_cycle_cont == True:
        big_cycle_cont = False
        counter = 0
        big_counter+=1
        while counter <= list_length - 1 - big_counter:
                if sorted_list[counter] < sorted_list[counter + 1]:
                    sorted_list[counter], sorted_list[counter + 1] = sorted_list[counter + 1], sorted_list[counter]
                    big_cycle_cont = True
                counter +=1
    return sorted_list
print(list_sort(my_list))
#print(my_list)
#ДЗ: бабл-сорт, який сортує в порядку спадання
