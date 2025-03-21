#PASSWORDGUESSR
import random
pin = "123"
n = len(pin) 
for i in range(10**n):
    num =str(10**n+i)[1:]
    if num == pin:
        print( "your pin is "+ pin)
        break
    else:
        print("wrong!")