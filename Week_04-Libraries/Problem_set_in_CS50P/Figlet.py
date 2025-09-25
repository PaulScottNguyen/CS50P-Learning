from pyfiglet import Figlet
#Package pyfiglet

def figlet_converter(converted_text, inputted_fontname):
    figlet = Figlet(font=inputted_fontname)
    return figlet.renderText(converted_text)

def main():
    fontname = input("What font?: ")
    text = input("Input: ")
    print(figlet_converter(text, fontname))

if __name__ == "__main__":
    main()
