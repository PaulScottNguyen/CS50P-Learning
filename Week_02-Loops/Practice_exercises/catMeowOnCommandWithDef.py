def main():
    meow(get_number()) #Function inside function


def get_number():
    while True:
        n = int(input("What's n? ")) #Ask for an int
        if n > 0: #If int is >0 then get out of loop
            return n
        #Else keep asking


def meow(n):
    for i in range(n): #Range n
        print("meow") #Print n meows


main()