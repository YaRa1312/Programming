import math

bot_name="Bob"
bot_age=19
bot_height=171
user_name=input("What is your name? ")
print("Hello, " + user_name + "! " + "My name is " + bot_name)
user_age=input("How old are you? ")
user_age=int(user_age)
print(type(user_age))
if bot_age<user_age:
    print("You are old.")
else:
    if bot_age==user_age:
        print("We are peers.")
    else:
        print("You are a child.")
print("I like you.")
user_height=input("What is your height? ")
user_height=int(user_height)
print(type(user_height))
if bot_height<user_height:
    print("You are taller.")
else:
    if bot_height==user_height:
        print("We have the same height.")
    else:
        print("You are smaller.")
print("You are nice!")
print("Let's play! Make a number from 1 to 9")
answer=input("Is it greater than 5? ")
if answer==("No"):
    answer=input("Is it greater than 3? ")
    if answer==("No"):
        answer=input("Is it greater than 2? ")
        if answer==("No"):
            answer=input("Is it greater than 1? ")
            if answer==("No"):
                print("It is 1. I guessed!")
            else:
                print("It is 2. I guessed!")
        else:
            print("It is 3. I guessed!")
    else:
        answer=input("Is it greater than 4? ")
        if answer==("No"):
            print("It is 4. I guessed!")
        else:
            print("It is 5. I guessed!")
else:
    answer=input("Is it greater than 7? ")
    if answer==("No"):
        answer=input("Is it greater than 6? ")
        if answer==("No"):
            print("It is 6. I guessed!")
        else:
            print("It is 7. I guessed!")
    else:
        answer=input("Is it greater than 8? ")
        if answer==("No"):
            print("It is 8. I guessed!")
        else:
            print("It is 9. I guessed!")
number: int = 1
answer=input("Is it 1? ")
while answer==("No"):
    number=number+1
    answer=input("Is it " + str(number) + "? ")
    if number+1 == 9:
        break
print (number)
