from social_network_classes import SocialNetwork,Person
import os
import social_network_classes

def mainMenu():
    os.system('clear')
    print("")
    print("1. Create a new person")
    print("2. Send a new message to yourself, from another user")
    print("3. Manage my account")
    print("4. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    os.system('clear')
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Block someone")
    print("5. Send someone a message")
    print("6. View my messages")
    print("7. Delete messages")
    print("8. <- Go back ")
    print("********************************************************")
    return input("Please Choose a number: ")

def editAccountMenu():
    os.system('clear')
    print("")
    print("1. Edit my name")
    print("2. Edit my age")
    print("3. Edit my bio")
    print("4. View my details and bio")
    print("5. <- Go back ")
    print("********************************************************")
    return input("Please Choose a number: ")

def createAccountMenu():
    os.system('clear')
    print("")
    person_object = Person(input("Input name: "), input("\nInput age: "), input("\nInput bio: "), "0")
    return person_object
    
def addFriendMenu(social_network_object):
    os.system('clear')
    print("")
    print("Who would you like to add as a friend?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].bio)
    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def showFriendsMenu(social_network_object):
    os.system('clear')
    print("")
    counter = 0
    for i in range(len(social_network_object.list_of_people)):
        if social_network_object.list_of_people[i].isFriend == "1":
            print(str(counter+1) + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].bio)
            counter+=1
    return input(str(counter+1) + ". <- Go back \n********************************************************\nPlease Choose a number: ")

def blockMenu(social_network_object):
    os.system('clear')
    print("")
    print("Who would you like to block?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].bio)
    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def sendMessageMenu(social_network_object):
    os.system('clear')
    print("")
    print("Who would you like to send a message to?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].bio)
    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")
    
def selectSenderMenu(social_network_object):
    os.system('clear')
    print("")
    print("Who is the person sending the message?")
    for i in range(len(social_network_object.list_of_people)):
        print(str(i+1)  + ".", social_network_object.list_of_people[i].name, social_network_object.list_of_people[i].age, social_network_object.list_of_people[i].bio)
    print(str(len(social_network_object.list_of_people)+1) + ". <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")

def viewMessageMenu(user_object):
    os.system('clear')
    print("")
    print("Here are your messages:")
    for i in range(len(user_object.messagelist)):
        print(str(i+1) + ".", user_object.messagelist[i])
        print("")
        print("")
    return input(str(len(user_object.messagelist)+1) + ". <- Go back \n********************************************************\nPlease Choose a number: ")

def removeMessageMenu(user_object):
    os.system('clear')
    print("")
    print("Which message would you like to delete?")
    for i in range(len(user_object.messagelist)):
        print(str(i+1) + ".", user_object.messagelist[i])
        print("")
        print("")
    print(str(len(user_object.messagelist)+1) + ". <- Go back")
    print("********************************************************")
    return input("Please Choose a number: ")