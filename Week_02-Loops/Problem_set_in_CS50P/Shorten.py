def CutLetters(Text):
    LettersToCut = "aAeEoOuUiI"
    ShortenedText = ""
    
    for characters in Text:
        if characters not in LettersToCut:
            ShortenedText+=characters
    return ShortenedText

def main():
    Text=input("I will turn it into Twttr: ")
    print(CutLetters(Text))
main()