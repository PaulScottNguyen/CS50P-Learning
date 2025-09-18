#Ask for user input of x, y
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: #if value of x smaller than value of y then
    print("x is less than y")
elif x > y: #if value of x larger than value of y then 
    print("x is greater than y")
    #Run the code then close program
else: #all cases unmention
    print("x is equal to y")
    #Run the code then close program
"""
This code is correct and most efficient.
We use else because mathematically, x=y when x is not less or greater than y
"""