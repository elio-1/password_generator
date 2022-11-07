import string
import random
import argparse
import sys
import pyperclip


def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument(
        "-n", default=12, help="Specify the length of your password", type=int
    )
    parser.add_argument(
        "-a",
        "-all",
        help="Generate password with ascii, digits and punctuations",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "-ascii",
        help="Add ascii letters to the generation pool | 0 for lower case | 1 for upper case | 2 for both",
        type=int,
        default=2,
        const=2,
        nargs='?',
        choices=[0, 1, 2],
    )
    parser.add_argument(
        "-i",
        "-digit",
        "-d",
        help="Add digits to the generation pool",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        "-punctuation",
        help="Add punctuation to the generation pool",
        action="store_true",
    )
    parser.add_argument(
        "-nocopy",
        help="Don't automaticaly copy into your clipboard",
        action="store_true",
    )
    parser.add_argument(
        '-output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file password in a .txt file"
    )
    
    args = parser.parse_args()

    chars = ""
    if args.a:
        chars = string.ascii_letters + string.digits + string.punctuation

    if args.c == 0:
        chars += string.ascii_lowercase
    if args.c == 1:
        chars += string.ascii_uppercase
    if args.c == 2:
        chars += string.ascii_letters

    if args.i:
        chars += string.digits

    if args.p:
        chars += string.punctuation

    if chars == '':
        chars = string.ascii_letters + string.digits + string.punctuation

    # generate the password    
    password = generator(chars, args.n)
    
    args.output.write(password)
    
    if args.nocopy:
        print("Your password: \n\n" + password + "\n")
    else:
        pyperclip.copy(password)
        print("Your password: \n\n" + password + "\n\nCopied into your clipboard!")


def generator(character_list, length):
    password = ""
    for _ in range(length):
        password = password + random.choice(character_list) 
    return password


if __name__ == "__main__":
    main()
