#!/usr/bin/env python3.6

import sys
import random
import string

# from user import User
# from credential import Credential

def passlen(l):
    _all = string.ascii_letters+ string.punctuation+string.digits
    return "".join(random.sample(_all,l))

def sign_in():
    username = input("Enter username: ")
    password1 = input("Enter password: ")
    password2 = input("Enter your password again: ")

    if password1 == password2:
        User(username, password1)
        return True
    else:
        print("Password doesn't match")
        sign_in()

def start():
    print("Start Here")
    options = True
    while options:
        inp = int(input("1. Sign In \n2. Exit"))
        if inp == 1:
            return sign_in()
            # options = False
        elif inp == 2:
            print("You are Signing Out")
            sys.exit(4)
        else:
            print("Select 1 or 2")

def main():
    print("Welcome to Password Locker")
    signed_in = start()
    if signed_in:
        signing_in = True
        while signing_in:
            
            choices = int(input("1. Create Account \n2. View Account \n3. Sign Out"))

            #Create Account
            if choices == 1:
                account = input("Enter account name: ")
                username = input("Enter your username: ")
                pass_len = passlen(lenpass)
                Credential(account, name, password)

            # #View Account
            # elif choices == 2:
            #     Credential.view()

    