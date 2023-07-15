from social_network_classes import SocialNetwork,User,Person
import social_network_ui
import os




#Create instance of main social network object
ai_social_network = SocialNetwork()
user = User("", "", "")
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            ai_social_network.add_account(social_network_ui.createAccountMenu())
        elif choice == "2":
            message_select = social_network_ui.messageView(ai_social_network)
            while True:
                if message_select == str(len(ai_social_network.list_of_people)+1):
                    break
                validd = False
                for i in range(len(ai_social_network.list_of_people)):
                    if message_select == str(i+1):
                        validd = True
                if validd == False:
                    message_select = social_network_ui.messageView(ai_social_network)
                else:
                    os.system('clear')
                    user.recieveMessage(input("What message do you want to send?\n\n"), ai_social_network.list_of_people[int(message_select)-1])
                    os.system('clear')
                    input("Message sent to " + user.name + ". Press enter to continue ")
                    message_select = social_network_ui.messageView(ai_social_network)
        elif choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    inner_inner_choice = social_network_ui.editAccountMenu()
                    while True:
                        if inner_inner_choice == "1":
                            os.system('clear')
                            user.name = input("Input Name: ")
                            os.system('clear')
                            inner_inner_choice = social_network_ui.editAccountMenu()
                        if inner_inner_choice == "2":
                            os.system('clear')
                            user.age = input("Input Age: ")
                            os.system('clear')
                            inner_inner_choice = social_network_ui.editAccountMenu()
                        if inner_inner_choice == "3":
                            os.system('clear')
                            user.bio = input("Input Bio: ")
                            os.system('clear')
                            inner_inner_choice = social_network_ui.editAccountMenu()   
                        if inner_inner_choice == "4":
                            os.system('clear')
                            print("Name:", user.name)
                            print("Age:", user.age)
                            print("Bio:", user.bio)
                            input("Press enter to go back\n")
                            os.system('clear')
                            inner_inner_choice = social_network_ui.editAccountMenu()
                        if inner_inner_choice == "5":
                            break
                        else:
                            inner_inner_choice = social_network_ui.editAccountMenu()
                if inner_menu_choice == "2":
                    inner_friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                    while True:
                        if inner_friend_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        validnum = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if inner_friend_choice == str(i+1):
                                validnum = True
                        if validnum == False:
                            inner_friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                        else:
                            user.add_friend(ai_social_network.list_of_people[int(inner_friend_choice)-1])
                            os.system('clear')
                            input("Friend Added! Press enter to continue ")
                            inner_friend_choice = social_network_ui.addFriendMenu(ai_social_network)
                if inner_menu_choice == "3":
                    social_network_ui.showFriends(user)
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                if inner_menu_choice == "4":
                    inner_block_choice = social_network_ui.blockView(ai_social_network)
                    while True:
                        if inner_block_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        validn = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if inner_block_choice == str(i+1):
                                validn = True
                        if validn == False:
                            inner_block_choice = social_network_ui.blockView(ai_social_network)
                        else:
                            user.block(ai_social_network, ai_social_network.list_of_people[int(inner_block_choice)-1])
                            os.system('clear')
                            input("Person blocked! Press enter to continue")
                            inner_block_choice = social_network_ui.manageAccountMenu()
                if inner_menu_choice == "5":
                    send_choice = social_network_ui.send_choice(ai_social_network)
                    while True:
                        if send_choice == str(len(ai_social_network.list_of_people)+1):
                            break
                        validnumber = False
                        for i in range(len(ai_social_network.list_of_people)):
                            if send_choice == str(i+1):
                                validnumber = True
                        if validnumber == False:
                            send_choice = social_network_ui.send_choice(ai_social_network)
                        else:
                            os.system('clear')
                            input("What message do you want to send?\n\n")
                            os.system('clear')
                            input("Message sent to " + ai_social_network.list_of_people[int(send_choice)-1].name + ". Press enter to continue ")
                            send_choice = social_network_ui.send_choice(ai_social_network)
                            
                if inner_menu_choice == "6":
                    viewchoice = social_network_ui.viewmessages(user)
                    while True:
                        if viewchoice == "1":
                            break
                        else:
                           viewchoice = social_network_ui.viewmessages(user) 
                if inner_menu_choice == "7":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "4":
            os.system('clear')
            print("Thank you for visiting. Goodbye")
            break

        else:
            choice = social_network_ui.mainMenu()
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
