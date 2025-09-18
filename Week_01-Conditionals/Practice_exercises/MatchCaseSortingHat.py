name = input("What's your name? ") #Ask for username

match name: 
    case "Harry" | "Hermione" | "Ron": #if name is in this case then execute the code
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?") #any value else