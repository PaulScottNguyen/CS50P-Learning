#Create an empty list called "Employees"
Employees = [] #No keys aka items

#A loop that runs 7 times, from i=0 to i=6
for i in range(7):
    #Each time ask for a string input that will be lowered case, strip all whitespaces before & after,
    #then capitalize the initials
    #Add an index counter i+1 to indicate the employee number
    Employee = str(input(f"Please enter employee number {i+1}: ")).lower().strip().title()
    
    #In case "\n" aka no input then skip to the next i range
    if Employee == "":
        continue #Skip to the next i range
    
    Employees.append(Employee) #Add string into the list "Employees"

#Prompt the user about the list being ordered in alphabetical method
print(f"The following employee list is in alphabetical order:\n") #"\n" means go to new line

#Another loop that run "name" times
#Index variable will start=1 using enumerate() Function to start counting
#Sorted() Function will sort everything in the list in an alphabetical order
for index, name in enumerate(sorted(Employees), start=1):
    #Start printing each employee name
    print(f"{index}. {name}")