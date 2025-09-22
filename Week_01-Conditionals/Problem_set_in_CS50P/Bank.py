#Output Hello
print(f"Hello, this is GSM Bank!")
greet = str(input("Greeting: ")) #Wait for the user's respones
match greet.lower(): #Lowercase the data in "greet"
    case "hello"|"hi"|"hey":
        print("you no manner no money for you")
    case "howdy"|"yeehaw":
        print("Yes you from Texas? Here is your money")
    case "good morning"|"good afternoon"|"good evening":
        print("You are so polite, here is the bank's vault key")
    case _: #All cases left
        print("You are not polite, no money for you")