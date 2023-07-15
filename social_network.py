from social_network_classes import SocialNetwork,User,Person
import social_network_ui
import os

#Create instance of main social network object
ai_social_network = SocialNetwork()

#Create the user
user = User("my_name", "my_age", "my_bio")

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    
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
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        if edit_detail_choice == "2":
                            os.system('clear')
                            user.age = input("Input Age: ")
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        if edit_detail_choice == "3":
                            os.system('clear')
                            user.bio = input("Input Bio: ")
                            edit_detail_choice = social_network_ui.editAccountMenu()   
                        if edit_detail_choice == "4":
                            os.system('clear')
                            print("Name:", user.name)
                            print("Age:", user.age)
                            print("Bio:", user.bio)
                            input("Press enter to go back\n")
                            edit_detail_choice = social_network_ui.editAccountMenu()
                        if edit_detail_choice == "5":
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
                            user.addFriend(ai_social_network.list_of_people[int(friend_choice)-1])
                            os.system('clear')
                            input("Friend Added! Press enter to continue ")
                            friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                if edit_account_choice == "3":
                    show_friends_choice = social_network_ui.showFriendsMenu(user)
                    while True:
                        if show_friends_choice == str(len(user.friendlist)+1):
                            break
                        else:
                            show_friends_choice = social_network_ui.showFriendsMenu(user)
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
                            block_choice = social_network_ui.manageAccountMenu()
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
                    break
                else:
                    edit_account_choice = social_network_ui.manageAccountMenu()
        elif choice == "4":
            os.system('clear')
            print("Thank you for visiting. Goodbye")
            break
        else:
            choice = social_network_ui.mainMenu()
        choice = social_network_ui.mainMenu()



        
