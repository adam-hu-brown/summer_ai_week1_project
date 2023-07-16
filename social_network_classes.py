import os
import json
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] 

    def createAccount(self, person_object):
        self.list_of_people.append(person_object)

    def save_social_media(self, user_object):
        with open('list_of_people.json', 'w') as f:
            data = json.dumps([person.__dict__ for person in self.list_of_people], indent=2, sort_keys=True)
            f.write(data)
        with open('messagelist.json', 'w') as f:
            data = json.dumps([message for message in user_object.messagelist], indent=2, sort_keys=True)
            f.write(data)
        with open('user_info.json', 'w') as f:
            data = json.dumps([user_object.__dict__], indent=2, sort_keys=True)
            f.write(data)

    def reload_social_media(self, user_object):
        with open('list_of_people.json', 'r') as f:
            data = f.read()
            data = json.loads(data)
            for i in data:
                self.createAccount(Person(str(i['name']), str(i['age']), str(i['bio']), str(i['isFriend'])))
        with open('messagelist.json', 'r') as f:
            data = f.read()
            data = json.loads(data)
            for message in data:
                user_object.messagelist.append(message)
 

        

class User:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
        self.messagelist = []

    def block(self, social_network_object, person_object):
        social_network_object.list_of_people.remove(person_object)

    def recieveMessage(self, message, person_object):
        self.messagelist.append("From " + person_object.name + ":\n      " + message)

class Person:
    def __init__(self, name, age, bio, isFriend):
        self.name = name
        self.age = age
        self.bio = bio
        self.isFriend = isFriend