#x = 5
#if x < 10:
#    print ('Smaller')
#if x > 20:
#    print ('Bigger')
#print ('Finish')

#n = 5
#while n > 0:
#    print (n)
#    n = n - 1
#print ('Blastoff!')

#eee = 'hello ' + 'there'
#eee = eee + ' 1'
#print (eee)

#sval = '123'
#type (sval)
#ival = int (sval)
#type (ival)
#print (ival + 1)

#nam = input ("What's your name?  ")
#print ("Welcome, nam")

#inp = input ('Europe floor? ')
#usf = int (inp) + 1
#print ('US floor ', usf)

#ДЗ 2.1.
#hrs = input ("Enter Hours: ")
#hrs = float (hrs)
#rate = input ("Enter Rate: ")
#rate = float (rate)
#p = hrs * rate
#print ("Pay: " + str(p))

#x = 5
#if x == 5:
#    print ('Is 5')
#    print ('Is Still 5')
#    print ('Third 5')

#ДЗ 3.1.
#hrs = input("Enter Hours: ")
#h = float(hrs)
#rate = input("Enter Rate: ")
#r = float(rate)
#if h >= 40:
#    if h == 40:
#        p = h * 40
#    else:
#        x = h - 40
#        p = (x*r*1.5) + (40*r)
#else:
#    p = h*r
#p = float(p)
#print (p)

#ДЗ 3.2.
#score = input("Enter Score: ")
#s = float (score)
#if s > 1:
#    print ("Try again. ")
#    quit ()
#else:
#    if s < 0:
#        print ("Try again. ")
#        quit ()
#    else:
#        if s < 0.6:
#            s = "F"
#        else:
#            if s >= 0.6:
#                if s >= 0.7:
#                    if s >= 0.8:
#                        if s >= 0.9:
#                            s = "A"
#                        else:
#                            s = "B"
#                    else:
#                        s = "C"
#                else:
#                    s = "D"
#print (s)

#def func (x):
#    print (x)
#print (func (10))
#print (func (20))

#def stuff():
#    print ("Hello")
#    return
#    print ("World")
#print (stuff())

#def addtwo (a, b):
#    added = a + b
#    return a
#x = addtwo (2, 7)
#print (x)

#ДЗ 4.1
#def computepay(h,r):
#    if h < 40:
#        return h*r
#    else:
#        x = h-40
#        return x*r*1.5 + 40*r

#hrs = input("Enter Hours: ")
#h = float (hrs)
#rate = input ("Enter Rate: ")
#r = float (rate)
#p = computepay(h,r)
#print("Pay ",p)

#while True:
#    line = input ('> ')
#    if line [0] == "#":
#        continue
#    if line == 'done':
#        break
#    print (line)
#print ("Done!")

#підрахування суми
#zork = 0
#print ("Before", zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + thing
#    print (zork, thing)
#print ("After", zork)

#визначення середнього арифметичного
#count = 0
#sum = 0
#print ("Before", count, sum)
#for value in [9, 41, 12, 3, 74, 15]:
#    count = count + 1
#    sum = sum + value
#    print (count, sum, value)
#print ("After", count, sum, sum/count)

#пошук потрібних значень
#print ("Before")
#for value in [9, 41, 12, 3, 74, 15]:
#    if value > 20:
#        print ("Large number", value)
#print ("After")

#пошук певного числа
#found = False
#print ("Before", found)
#for value in [9, 41, 12, 3, 74, 15]:
#    if value == 3:
#        found = True
#        break
#    print (found, value)
#print ("After", found)

#визначення найбільшого числа
#largest_so_far = -1
#print ("Before", largest_so_far)
#for the_num in [9, 41, 12, 3, 74, 15]:
#    if the_num > largest_so_far:
#        largest_so_far = the_num
#    print (largest_so_far, the_num)
#print ("After", largest_so_far)

#визначення найменшого числа
#smallest = None
#print ("Before", smallest)
#for value in [9, 41, 12, 3, 74, 15]:
#    if smallest is None:
#        smallest = value
#    elif value < smallest:
#        smallest = value
#    print (smallest, value)
#print ("After", smallest)

#tot = 0
#for i in [5, 4, 3, 2, 1]:
#    tot = tot + 1
#print (tot)

#ДЗ 5.2 [7, 2, bob, 10, 4]
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    num = int()
    if num is str ():
        print ("Invalid input")
    if largest is None:
        largest = num
    else:
        if num > largest:
            largest = num
    if smallest is None:
        smallest = num
    else:
        if num < smallest:
            smallest = num
    if num == "done" :
        break
    print(num)

print("Maximum is ", largest)
print("Minimum is ", smallest)
