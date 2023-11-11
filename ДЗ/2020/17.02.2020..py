def ask (a, b):
    if a==b:
        print("Answer is " + str(a))
    else:
        while True:
            answer=input ("Is the number greater than " + str((a+b)//2) + "? ")
            if answer=="Yes" or answer=="No":
                break
        if answer == "Yes":
            ask ((a+b)//2+1, b)
        else:
            ask (a, (a+b)//2)
ask (1,100)
