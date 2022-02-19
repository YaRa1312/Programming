#def is_number(s):
#  try:
#    float(s)
#    return True
#  except ValueError:
#    return False

"""input_list = []

while len(input_list) < 7:
  print("Input float number:")
  s = input()
  if (is_number(s)):
    input_list.append(s)
  else:
    print("No, that's not float, try again...")

print(input_list)

sorted_list = input_list.copy()
sorted_list.sort(reverse = True)

sorted_dict = {}
for i in range(len(input_list)):
  sorted_dict[input_list[i]] = sorted_list[i]

print(sorted_dict)"""

def recursion_f(s, counter):
  if (counter >= 0):
    counter -= 1
    return s + recursion_f(s, counter)
  else:
    return ""

print(recursion_f('as', 6))
