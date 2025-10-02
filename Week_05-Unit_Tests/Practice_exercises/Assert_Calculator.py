from Calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4 #Assert that 2^2=4, else print assertion error
    assert square(3) == 9


if __name__ == "__main__":
    main()