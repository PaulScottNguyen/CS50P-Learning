x = float(input("What's x? ")) #Ask the user for value of float x
y = float(input("What's y? ")) #Ask the user for value of float y

#Compute x+y then round the result, after that put it in "z"
z = round(x + y) 

print(z) #print the answer "z"

"""
Input: 2.2, 2.4
Compute: 
    1. x+y=4.6 then round it to the nearest int which is 5
    2. Put 5 into variable "z"
Output: 5
"""
#This is what will happen if we use the code

#The arguments for round is round(number,[ndigits])
#Ex: round(x+y, 2) will round the number to two digits after decimal
