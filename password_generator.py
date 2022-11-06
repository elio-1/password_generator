import string
import random
import sys
import pyperclip

def main():
    chars = ''
    all_char = string.ascii_letters + string.digits + string.punctuation

    if len(sys.argv) == 1:
        generator(all_char, 14)
    if len(sys.argv) > 5:
        helper()
    if sys.argv[1] == 'h' or sys.argv[1] == '-h' or sys.argv[1] == 'help':
        helper()
    if len(sys.argv) == 5:
        generator(all_char, get_length())
    if len(sys.argv) == 4:
        chars = chars + add_chars(sys.argv[2])
        chars = chars + add_chars(sys.argv[3])
    if len(sys.argv) == 3:
        chars = chars + add_chars(sys.argv[2])
    if len(sys.argv) == 2:
        generator(all_char, get_length())
    
    generator(chars, get_length())
    

def add_chars(char):
    match char:
            case "ascii" | "-ascii" | "asc" | "letters" | '-l'| '-c':
                return string.ascii_letters
            case "digits" | "d" | "-d" | "-digits" | "digit" | "-digit"|'-i':
                return string.digits
            case "punctuation" | "p" | "-p":
                return string.punctuation
            case "all" | "a" | '-a' | "-all":
                return string.ascii_letters + string.digits + string.punctuation
            case _:
                helper()

def get_length():
    try:
        return int(sys.argv[1])
    except (IndexError) (ValueError):
        helper()

def helper():
    print("Usage: python3 password_generator.py (optional:) [length] [all/ascii/digits/punctuations] [ascii/digits/punctuations] [ascii/digits/punctuations]")
    print("python3 password_generator.py 16 -all")
    print("python3 password_generator.py 12 ascii digits")
    sys.exit()

def generator(character_list, length):
    password = ''
    for i in range(length):
        password = password + random.choice(character_list)
    pyperclip.copy(password)
    print("Your password: \n\n" + password + "\n\nCopied into your clipboard!")

if __name__ == "__main__":
    main()