"""try:
    float(s)
    return True
except ValueError:
    return False"""

"""def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False"""

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

input_list = []
while len(input_list) < 7:
  print("Input float number:")
  s = input()
  if (is_number(s)):
    input_list.append(s)
  else:
    print("No, that's not float, try again...")

print(input_list)

sorted_list = input_list.copy()
def list_sort (sorted_list):
    """for i in range (0, len(sorted_list)-1):
        for j in range (0, len(sorted_list)-1-i):
            if sorted_list[j] < sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return(sorted_list)"""
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
print(list_sort(input_list))

sorted_dict = {}
for i in range(len(input_list)):
    sorted_dict[sorted_list[i]] = input_list[i]

print(sorted_dict)

sorted_list = list(dict.fromkeys(sorted_list))
print(sorted_list)

def recursion_f(s, counter):
  if (counter >= 0):
    counter -= 1
    return s + recursion_f(s, counter)
  else:
    return ""
print(recursion_f('you', 6))
