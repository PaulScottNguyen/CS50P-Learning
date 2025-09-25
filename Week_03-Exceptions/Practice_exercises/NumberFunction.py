def main():
    x = get_int() #Function get_int
    print(f"x is {x}")


def get_int(): #Define function
    while True:
        try:
            return int(input("What's x?"))
            #Will return x and get out of loop
        except ValueError:
            print("x is not an integer")
            #Will loop and ask again


main()