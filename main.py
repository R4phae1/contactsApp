
import json

class ContactManager:

    def __init__(self):
        self.contacts = []

    def loadContacts(self):
        with open('./contacts.json', "r+") as f:
            data = json.load(f)
        for item in data:
            tmpContact = Contact(item["firstName"], item["lastName"], item["number"])
            self.contacts.append(tmpContact)

    def saveContacts(self):
        saveData = []
        for item in self.contacts:
            saveData.append(item.toJSON())
        print(saveData)
        with open('./contacts.json', "w") as f:
            json.dump(saveData, f)

    def displayAllContacts(self):
        for item in self.contacts:
            print(item)

    def addContact(self, firstName, lastName, number):
        tmpContact = Contact(firstName, lastName, number)
        self.contacts.append(tmpContact)

    def deleteContact(self, contact):
        pass

    def searchContact(self, firstName, lastName):
        pass

class Contact:

    def __init__(self, firstName="", lastName="", number=""):
        self.number = number
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"First name: {self.firstName}\nLast name: {self.lastName}\nPhone number: {self.number}\n"
    
    def toJSON(self):
        tmp = {}
        tmp["firstName"] = self.firstName
        tmp["lastName"] = self.lastName
        tmp["number"] = self.number
        return tmp

def main():
    myContactManager = ContactManager()
    myContactManager.loadContacts()
    myContactManager.displayAllContacts()
    firstName = input("insert FirstName")
    lastName = input("insert LastName")
    number = input("insert Number")
    myContactManager.addContact(firstName, lastName, number)
    myContactManager.displayAllContacts()
    myContactManager.saveContacts()

main()

