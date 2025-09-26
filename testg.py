def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEOUIaeoui":
            translation = translation + "g"
        else:
            translation  = translation + letter
        return translation
    
def main():
    string = input("Write something: ")
    translate(string)
    print(string)
main ()