"""
x = input("What's x? ") #Ask the user for value of x
y = input("What's y? ") #Ask the user for value of y
z = x + y
print(z)

"""
#The above code will work but default data type is string

"""
Input: 1, 2
Compute: 
    1. The program combines two strings and put in variable "z"
Output: 123
"""
#This is what will happen if we use that code

#Correct way
x = int(input("What's x? ")) #Ask the user for value of int x
y = int(input("What's y? ")) #Ask the user for value of int y
z = x + y #Compute x+y and put in variable "z"
print(z) #print the answer "z"

#This program is using int data type, only allow whole numbers
#For decimal numbers, use float data type