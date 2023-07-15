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
                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
