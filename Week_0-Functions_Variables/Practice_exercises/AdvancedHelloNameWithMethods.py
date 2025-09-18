#Ask user for their name
name = input("What's your name?") 
#Save user input in variable "name"

#Strip whitespaces before and after the name
#Capitalize the first word of the string
#Recontain the new data inside the existing variable "name"
name = name.strip().lower().title()

#Output "Hello <name>"
print(f"Hello {name}")

"""
Input: "           pAUl      " (note: quotes sign to show whitespaces)
Compute: 
    1. The program strip all whitespaces before and after "pAUl"
    2. The program then lowercase all text to "paul"
    3. The program then capitalize the first character "Paul"
Output: "Hello Paul"
"""
