# You can implement user interface functions here.
from social_network_classes import SocialNetwork,Person
import os
import social_network_classes

def mainMenu():
    os.system('clear')
    print("")
    print("1. Create a new person")
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
    print("4. Block someone")
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

def createAccountMenu():
    os.system('clear')
    print("")
    newPerson = Person(input("Input name: "), input("\nInput age: "), input("\nInput bio: "))
    return newPerson
    
def addFriendMenu(social_network_object):
    os.system('clear')
    print("")
    print("Who would you like to add as a friend?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].age)

    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")

    return input("Please Choose a number: ")

def showFriends(user_object):
    os.system('clear')
    print("")
    for i in range(len(user_object.friendlist)):
        print(str(i+1) + ".", user_object.friendlist[i].name, user_object.friendlist[i].age, user_object.friendlist[i].bio)
    input("Press enter to go back ")

def blockView(social_network_object):
    os.system('clear')
    print("")
    print("Who would you like to block?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].age)

    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")

    return input("Please Choose a number: ")