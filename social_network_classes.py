import os
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] 
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    def createAccount(self, person_object):
        self.list_of_people.append(person_object)

    ## For more challenge try this
    def reload_social_media(self):
        pass
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.

class User:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
        self.friendlist = []
        self.messagelist = []

    def block(self, social_network_object, person_object):
        social_network_object.list_of_people.remove(person_object)

    def addFriend(self, person_object):
        self.friendlist.append(person_object)

    def recieveMessage(self, message, person_object):
        self.messagelist.append("From " + person_object.name + ":\n      " + message)

class Person:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio