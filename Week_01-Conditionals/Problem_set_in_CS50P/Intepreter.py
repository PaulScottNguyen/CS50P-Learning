#Function to do addition
def addition(x, y):
    return (x+y)

#Function to do subtraction
def subtraction(x, y):
    return (x-y)

#Function to do multiplication
def multiplication(x, y):
    return (x*y)

#Function to do divison
def divison(x, y):
    if y==0:
        return "Cannot divide by 0, please try again!"
    else:
        return (x/y)

#Function to do modulo
def modulo(x, y):
    return (x%y)


#Function to convert the expression into two variables by splitting at +;-;*;/;%
def calculate(TheExpression):
    TheExpression = TheExpression.replace(" ","") #Delete all whitespaces in between of the string
    if '+' in TheExpression:
        x, y = TheExpression.split('+') #Split the string into two strings right at +
        return addition(float(x), float(y)) #Convert datatype of two new strings into float
        
    elif '-' in TheExpression:
        x, y = TheExpression.split('-') #Split the string into two strings right at -
        return subtraction(float(x), float(y)) #Convert datatype of two new strings into float

    elif '*' in TheExpression:
        x, y = TheExpression.split('*') #Split the string into two strings right at *
        return multiplication(float(x), float(y)) #Convert datatype of two new strings into float

    elif '/' in TheExpression:
        x, y = TheExpression.split('/') #Split the string into two strings right at /
        return divison(float(x), float(y)) #Convert datatype of two new strings into float

    elif '%' in TheExpression:
        x, y = TheExpression.split('%') #Split the string into two strings right at %
        return modulo(float(x), float(y)) #Convert datatype of two new strings into float
    else:
        return False #If cant find any signs above or an invalid symbol

        

def main():
    #Ask user for math expression, can be +;-;*;/;%
    AnExpression = str(input("Please enter your expression (Only x+y; x-y; x*y; x/y; or x%y): ")).strip().lower()
    Result = calculate(AnExpression)
    if Result == False: #For invalid input
        print(f"Invalid mathematical expression") 
    else: #Will work
        print(f"The result of {AnExpression} is {Result}")
main()