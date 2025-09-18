def main(): #Define main function
    UserInput = str(input(f"Hello:)")).strip().lower() #User input
    if UserInput == "hello:)":
        print(f"Hello 😀")
    elif UserInput == "goodbye:(":
        print(f"Goodbye 😞")
    elif UserInput == "hello:) goodbye:(":
        print(f"Hello 😀 Goodbye 😞")
    else:
        print(f"Hmm?")
main() #Call main function