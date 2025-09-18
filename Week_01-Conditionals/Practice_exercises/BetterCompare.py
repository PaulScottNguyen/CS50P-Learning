#Ask for user input of x, y
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: #if value of x smaller than value of y then
    print("x is less than y")
if x > y: #if value of x larger than value of y then
    print("x is greater than y")
if x == y: #if value of x is equal to value of y then
    print("x is equal to y")
"""
This code is correct, however it is not efficient as it has to ask three times
before shutting down the program.
"""