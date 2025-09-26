
import emoji

def main():
    user_input = input("Input: ")
    # Convert emoji codes and aliases to actual emoji
    output = emoji.emojize(user_input, language='alias')
    print("Output:", output)

if __name__ == "__main__":
    main()
