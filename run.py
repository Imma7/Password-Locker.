#!/usr/bin/env python3.6

import sys
import random
import string

from user import User
from credential import Credential

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
        print('\n')
        print("Password doesn't match")
        print('\n')
        sign_in()

def start():
    print("Start Here")
    options = True
    while options:
        inp = int(input("1. Sign In \n2. Exit"))
        print('\n')
        if inp == 1:
            return sign_in()
            # options = False
        elif inp == 2:
            print('\n')
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
            
            print('\n')
            choices = int(input("1. Create Account \n2. View Account \n3. Delete Account \n4. Sign Out"))

            #Create Account
            if choices == 1:
                account = input("Enter account name: ")
                username = input("Enter your username: ")
                password_len = int(input("Ener password length: "))
                password = passlen(password_len)
                Credential(account, username, password)

            #View Account
            elif choices == 2:
                Credential.view_account()

            #Delete Account
            elif choices == 3:
                Credential.delete_account(input("Which account do you wish to delete ?"))

            #Sign Out
            elif choices == 4:
                print('-'*40)
                print("You are exiting. Bye :)")
                signing_in = False

if __name__ == '__main__':
    main()
    