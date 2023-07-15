# You can implement user interface functions here.
from social_network_classes import SocialNetwork
import os

def mainMenu():
    os.system('clear')
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    os.system('clear')
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")

def editAccountMenu():
    os.system('clear')
    print("")
    print("1. Edit my name")
    print("2. Edit my age")
    print("3. Edit my bio")
    print("4. View my details and bio")
    print("5. <- Go back ")
    return input("Please Choose a number: ")
    