x = int(input("What's x? "))
print(f"x is {x}")
#This code normally works, however
#If we run this program and type “cat”, 
# we’ll see ValueError: invalid literal for int() with base 10: 'cat'.
# In other words, the int function cannot convert the text “cat” into a number.