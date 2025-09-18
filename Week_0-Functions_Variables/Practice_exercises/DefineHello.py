#Create a new function "hello" that takes "username" as argument
def hello(username): 
    print("Hello", username)

# Ask user for their name, remove whitespace from the str, lowercase all and capitalize the first letter of each word
def main():
    name = input("What's your name? ").strip().lower().title()
    hello(name)
#Call function "hello" and put the data of "name" into variable "username"
#The function then print "Hello <username>"

main() #main() to call the function main to run the program