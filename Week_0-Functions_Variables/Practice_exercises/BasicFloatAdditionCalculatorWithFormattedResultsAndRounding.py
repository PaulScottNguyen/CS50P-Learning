x = float(input("What's x? ")) #Ask the user for value of float x
y = float(input("What's y? ")) #Ask the user for value of float y

#Compute x+y then round the result, after that put it in "z"
z = round(x + y, 2) 

print(f"{z:,}") #print the answer "z" in formatted result
#Ex: 1,000,000 so it is easier to look at
#Syntax print(f"<variable>:,")

"""
Input: 4096.35278, 16384.655179
Compute: 
    1. x+y then round it to 2 numbers after decimal
    2. Put result into variable "z"
Output: 20,481.01
"""
#This is what will happen if we use the code
