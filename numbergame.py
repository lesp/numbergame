"""
This number game will accept any integer as input, and then run a
series of calculations which will always return the answer 3

This game was suggested by Caleb, aged 9, from Mereside Primary School, Blackpool

"""

from time import sleep
number = int(raw_input("Think of a number :"))
print("You chose "+str(number))
sleep(1)
print("I will double it to "+str(number*2))
double = number * 2
sleep(1)
print("I will now add 9 to that number "+str(double+9))
plusnine = double + 9
sleep(1)
print("I will now subtract 3 from that number "+str(plusnine-3))
minusthree = plusnine - 3
sleep(1)
print("I will now divide by 2 "+str(minusthree/2))
dividetwo = minusthree / 2
sleep(1)
print("Now I will subtract your original answer ")
answer = dividetwo - number
sleep(1)
print answer
