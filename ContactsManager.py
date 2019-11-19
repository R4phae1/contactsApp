import json

class ContactManager:
    def __init__(self):
        self.contacts = []


    def loadContacts(self):
        try:
            with open('contacts.json', "r+") as f:
                data = json.load(f)
                for item in data:
                    tmpContact = Contact(item["firstName"], item["lastName"], item["number"])
                    self.contacts.append(tmpContact)
        except:
            pass


    def saveContacts(self):
        saveData = []
        for item in self.contacts:
            saveData.append(item.toJSON())

        with open('contacts.json', "w") as f:
            json.dump(saveData, f)


    def displayAllContacts(self):
        for idx, item in enumerate(self.contacts):
            print("Index:", idx, "\n", item.str())


    def addContact(self, firstName, lastName, number):
        tmpContact = Contact(firstName, lastName, number)
        self.contacts.append(tmpContact)


    def deleteContact(self, contact_idx):
        self.contacts.remove(self.contacts[contact_idx])


    def searchContact(self, firstName, lastName):
        for item in self.contacts:
            if item.firstName == firstName and item.lastName == lastName:
                print(item.str())


class Contact:
    def __init__(self, firstName="", lastName="", number=""):
        self.number = number
        self.firstName = firstName
        self.lastName = lastName


    def str(self):
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

    if len(myContactManager.contacts) == 0:
        print("There are no contact. You should add.")
        q = "2"
    else:
        q = input("Select HI! press 1 to search - 2 for adding a contact - 3 for deleting a contact: ")

    if q == "1":
        firstName = input("insert FirstName: ")
        lastName = input("insert LastName: ")
        myContactManager.searchContact(firstName,lastName)

    elif q == "2":
        firstName = input("insert FirstName: ")
        lastName = input("insert LastName: ")
        number = input("insert Number: ")
        myContactManager.addContact(firstName, lastName, number)
        myContactManager.saveContacts()

    elif q == "3":
        myContactManager.displayAllContacts()
        delete_index = int(input("Select index for deleting contact: "))
        try:
            myContactManager.deleteContact(delete_index)
            myContactManager.saveContacts()
        except:
            print("Wrong input. exiting...")

    else:
        print("Wrong input. exiting...")


main()