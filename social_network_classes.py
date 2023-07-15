# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
import os
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass
    def add_account(self, person_object):
        self.list_of_people.append(person_object)

    ## For more challenge try this
    def reload_social_media(self):
        pass
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
   # def create_account(self, person_object):
    #    self.list_of_people.append(person_object)

class User:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
        self.friendlist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        #implement sending message to friend here
        pass

class Person:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio