from social_network_classes import SocialNetwork,User,Person
import social_network_ui
import os
import json
import time
import sys

#Create instance of main social network object
ai_social_network = SocialNetwork()

#Create the user
user = User("my_name", "my_age", "my_bio")
ai_social_network.reload_social_media(user)
with open('user_info.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
    for i in data:
        user.name = i['name']
        user.age = i['age']
        user.bio = i['bio']
if user.name == "my_name":
    print("")
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    print("")
    print("Let's start by creating your account. ")
    print("")
    user.name = input("Input your name: ")
    print("")
    user.age = input("Input your age: ")
    print("")
    user.bio = input("Input your bio: ")
    os.system('clear')
    create_message = "Creating your account.."
    print(create_message)
    for i in range(20):
        os.system('clear')
        create_message = create_message + "."
        print(create_message)
        time.sleep(0.25)
    os.system('clear')
        


if __name__ == "__main__":
    choice = social_network_ui.mainMenu()
    while True: 
        if choice == "1":
            ai_social_network.createAccount(social_network_ui.createAccountMenu())
        elif choice == "2":
            sender_choice = social_network_ui.selectSenderMenu(ai_social_network)
            while True:
                if sender_choice == str(len(ai_social_network.list_of_people)+1):
                    break
                valid_sender_choice = False
                for i in range(len(ai_social_network.list_of_people)):
                    if sender_choice == str(i+1):
                        valid_sender_choice = True
                if valid_sender_choice == False:
                    sender_choice = social_network_ui.selectSenderMenu(ai_social_network)
                else:
                    os.system('clear')
                    user.recieveMessage(input("What message do you want to send?\n\n"), ai_social_network.list_of_people[int(sender_choice)-1])
                    os.system('clear')
                    input("Message sent to " + user.name + ". Press enter to continue ")
                    sender_choice = social_network_ui.selectSenderMenu(ai_social_network)
        elif choice == "3":
            edit_account_choice = social_network_ui.manageAccountMenu()
            while True:
                if edit_account_choice == "1":
                    edit_detail_choice = social_network_ui.editAccountMenu()
                    while True:
                        if edit_detail_choice == "1":
                            os.system('clear')
                            user.name = input("Input Name: ")
                            os.system('clear')
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        elif edit_detail_choice == "2":
                            os.system('clear')
                            user.age = input("Input Age: ")
                            os.system('clear')
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        elif edit_detail_choice == "3":
                            os.system('clear')
                            user.bio = input("Input Bio: ")
                            os.system('clear')
                            edit_detail_choice = social_network_ui.editAccountMenu()   
                        elif edit_detail_choice == "4":
                            os.system('clear')
                            print("Name:", user.name)
                            print("Age:", user.age)
                            print("Bio:", user.bio)
                            input("Press enter to go back\n")
                            os.system('clear')
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        elif edit_detail_choice == "5":
                            break
                        else:
                            edit_detail_choice = social_network_ui.editAccountMenu()
                if edit_account_choice == "2":
                    friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                    while True:
                        if friend_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        valid_friend_choice = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if friend_choice == str(i+1):
                                valid_friend_choice = True
                        if valid_friend_choice == False:
                            friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                        else:
                            ai_social_network.list_of_people[int(friend_choice)-1].isFriend = "1"
                            os.system('clear')
                            input("Friend Added! Press enter to continue ")
                            friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                if edit_account_choice == "3":
                    show_friends_choice = social_network_ui.showFriendsMenu(ai_social_network)
                    while True:
                        counter = 0
                        for i in range(len(ai_social_network.list_of_people)):
                            if ai_social_network.list_of_people[i].isFriend == "1":
                                counter+=1
                        if show_friends_choice == str(counter+1):
                            break
                        else:
                            show_friends_choice = social_network_ui.showFriendsMenu(ai_social_network)
                if edit_account_choice == "4":
                    block_choice = social_network_ui.blockMenu(ai_social_network)
                    while True:
                        if block_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        valid_block_choice = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if block_choice == str(i+1):
                                valid_block_choice = True
                        if valid_block_choice == False:
                            block_choice = social_network_ui.blockMenu(ai_social_network)
                        else:
                            user.block(ai_social_network, ai_social_network.list_of_people[int(block_choice)-1])
                            os.system('clear')
                            input("Person blocked! Press enter to continue")
                            block_choice = social_network_ui.blockMenu(ai_social_network)
                if edit_account_choice == "5":
                    send_choice = social_network_ui.sendMessageMenu(ai_social_network)
                    while True:
                        if send_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        valid_send_choice = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if send_choice == str(i+1):
                                valid_send_choice = True
                        if valid_send_choice == False:
                            send_choice = social_network_ui.sendMessageMenu(ai_social_network)
                        else:
                            os.system('clear')
                            input("What message do you want to send?\n\n")
                            os.system('clear')
                            input("Message sent to " + ai_social_network.list_of_people[int(send_choice)-1].name + ". Press enter to continue ")
                            send_choice = social_network_ui.sendMessageMenu(ai_social_network)             
                if edit_account_choice == "6":
                    view_choice = social_network_ui.viewMessageMenu(user)
                    while True:
                        if view_choice == str(len(user.messagelist)+1):
                            break
                        else:
                           view_choice = social_network_ui.viewMessageMenu(user) 
                if edit_account_choice == "7":
                    remove_choice = social_network_ui.removeMessageMenu(user)
                    while True:
                        if remove_choice == str(len(user.messagelist)+1):
                            break
                        valid_remove_choice = False
                        for i in range(len(user.messagelist)):
                            if remove_choice == str(i+1):
                                valid_remove_choice = True  
                        if valid_remove_choice == False:
                            remove_choice = social_network_ui.removeMessageMenu(user)
                        else: 
                            user.messagelist.remove(user.messagelist[int(remove_choice)-1])
                            os.system('clear')
                            input("Message deleted! Press enter to continue")
                            remove_choice = social_network_ui.removeMessageMenu(user)
                if edit_account_choice == "8":
                    break
                else:
                    edit_account_choice = social_network_ui.manageAccountMenu()
        elif choice == "4":
            ai_social_network.save_social_media(user)
            os.system('clear')
            print("Thank you for visiting. Goodbye")
            break
        else:
            choice = social_network_ui.mainMenu()
        choice = social_network_ui.mainMenu()
