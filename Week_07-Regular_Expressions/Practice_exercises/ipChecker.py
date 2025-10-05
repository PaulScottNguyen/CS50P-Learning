import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #pattern only allow 0-999
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    
    if not match:
        return False

    # Check each number is between 0 and 255
    for number in match.groups():
        if not 0 <= int(number) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()