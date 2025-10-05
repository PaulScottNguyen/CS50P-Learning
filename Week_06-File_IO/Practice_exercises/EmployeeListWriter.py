#import necessary stuff
import csv
import os

#Create an empty list called "Employees"
Employees = []

#This function will check if input is "\n", "/close", valid or invalid input
def CheckEmployee(Employee):
    #strip all whitespaces before and after string, then lowercase all
    raw_input = Employee.strip().lower()

    if raw_input == "": #if input is "\n"
        return False  # Skip empty input
    
    elif raw_input == "/close": #elif input is "/close"
        print("Saving your file...\n") #prompt user

        print(f"The following employee list:\n")
        OutList() #Run OutList() Function to show the Employees list of dictionaries
        
        print("\nClosing program...")
        exit() #Shutdown program
    
    else: #all other cases
        
        try: #If format is correct
            Datas = [Data.strip().title() for Data in Employee.split(",")]
            if len(Datas) != 4: #There must be 4 items in the Datas list
                raise ValueError
            name, title, number, email = Datas #Assign each item to a variable
            #Create a dictionary
            Employee_data = {
                "Name": name,
                "Title": title,
                "Phone Number": number,
                "Email": email
            }
            Employees.append(Employee_data) #Add the dictionary into the Employees list
            #A dict inside a list
            return True
            #Return True statement
        
        except ValueError: #If format raises ValueError
            print("Invalid format. Please use: full name, title, phone number, email")
            return False
            #Return False statement

def OutList():
    for index, name in enumerate(Employees, start=1):
        #Start printing each employee name
        print(f"{index}. {name}")

def main():
    i = 1 #Variable i=1
    #Prompt user
    print("WELCOME USER TO GSM EMPLOYEE LIST WRITER!\n")
    print("*Formatting: full name , title , phone number , email")
    print("Example: John Doe, CEO, 123456789, johndoe@gmail.com\n")

    while True:
        Employee = input(f"Please enter employee number {i} information: ")
        if CheckEmployee(Employee):
            i += 1 #Will add 1 into i if the Function return True
        

if __name__ == "__main__":
    main() #Call main Function