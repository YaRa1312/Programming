#f = open ("input.txt", "w+")
#f.write("My name is . I study at .")
f=open("input.txt", "a+")
user_name = input("What is your name? ")
user_un = input("Where do you study? ")
f.write("My name is " + user_name + ". I study at " + user_un + ".")
print(f.read())
print("My name is " + user_name + ". I study at " + user_un + ".")

#user_name = input("What is your name? ")
#user_un = input("Where do you study? ")
#my_file = open('input1.txt', 'r+')
#my_file.write(user_name + " " +  user_un)
#my_file.seek(0)
#print(my_file.read())
#print("My name is " + user_name + ". I study at " + user_un + ".")

#Input file: My name is.  I study at.
#User_name: Iryna
#User_university: KNU
#Output: My name is Iryna. I study at KNU.

#file = open('input.txt', 'a')
#print(file.read(4))
#print(file.tell())
#file.seek(1)
#print(file.tell())
#print(file.read())
