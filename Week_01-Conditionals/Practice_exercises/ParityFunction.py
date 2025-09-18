def main(): #Create function main
    x = int(input("What's x? ")) #Ask for user input of x
    if is_even(x): #if boolean True
        print("Even")
    else: #if boolean False
        print("Odd")


def is_even(n): #Create new function is_even
    if n % 2 == 0: #Even numbers divided by 2 will have the remainder of 0
        return True #Return boolean value of True
    else:
        return False #Return boolean value of False


main() #Call the function main