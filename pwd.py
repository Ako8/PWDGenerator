import string
import random


def generate_pwd(length, numbers=True, special_chars=True, capital=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ''
    for i in range(length):
        pwd += random.choice(characters)
    if capital:
        print(pwd.capitalize())
    else:
        print(pwd)


leng = int(input("How long pwd u want to be: "))
num = input("Want pwd to contain numbers? (y/n)").lower() == "y"
spc_chars = input("Want pwd to contain special characters? (y/n)").lower() == "y"


generate_pwd(leng, num, spc_chars, False)