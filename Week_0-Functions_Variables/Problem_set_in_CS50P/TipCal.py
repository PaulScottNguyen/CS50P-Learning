def main(): #Define main function
    #When user input the money => send to dollars_to_float function, then it return values to dollars
    dollars = dollars_to_float(input("How much was the meal? ")) 
    #When user input the percentage => send to percent_to_float function, then it return values to percent
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent #Calculate the tip
    print(f"Leave ${tip:.2f}") #Print the tip with 2 decimal digits

def dollars_to_float(d): #When data is in container "d", remove "$" and return it to dollars
    return float(d.replace("$",""))

def percent_to_float(p): #When data is in container "p", remove "%", divide by 100 and return it to percent
    return float(p.replace("%",""))/100

main() #Call main function