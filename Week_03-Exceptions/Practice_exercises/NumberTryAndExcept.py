while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

#This code will try first, if it encounters error it will loop and ask again
#It will get out of loop after getting x aka break