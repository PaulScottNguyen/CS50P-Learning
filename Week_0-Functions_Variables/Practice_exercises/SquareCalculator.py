#Create new function that will compute x square
def square(x): 
    return x * x


def main(): #The main function which the program will run
    x = int(input("What's x? ")) #Input int number
    answer = square(x) #New variable that hold the return value of function square
    print(f"Squared x is {answer}") #Output


main() #Call main to run the function