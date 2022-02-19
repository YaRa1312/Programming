number: int = 1
answer=input("Is it 1? ")
while answer==("No"):
    number=number+1
    answer=input("Is it " + str(number) + "? ")
    if number+1 == 10:
        break
print (number)

while True:
    answer=input("Is the number greater than 5? ")
    if answer=="Yes" or answer=="No":
        break

answer=" "
while (answer!="Yes" or answer!= "No"):
    answer=input("Is the number greater than 5? ")

word="HelloAL"
for counter in word:
    print(counter*5)
    if counter=="L":
        continue
    print ("Do you like it? ")

word = "abcte"
counter = 0
for letter in word:
    print (counter)
    if letter == "t":
        print ("There was t on " + str(counter) + " place. ")
        break
    counter += 1
else:
    print ("There  was no t in the word.")

numbers = [1, 2, 4, 5]
print (type (numbers))
max_item = numbers [0]
for item in numbers:
    if item>max_item:
        max_item = item
print (max_item)
