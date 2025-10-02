from Calculator import square
#open the Calculator.py file and import the function in it


def main():
    test_square() #A test function


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

#It will print if the function square encounter errors

if __name__ == "__main__":
    main()