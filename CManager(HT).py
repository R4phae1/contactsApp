import json

class HashTable(object):
    def __init__(self, length=32):
        self.array = [None] * length


    def hash(self, key):
        length = len(self.array)
        return hash(key) % length


    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])


    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()


    def is_empty(self):
        for key in self.array:
            if key != None:
                return False
        return True


    def last_elem_idx(self):
        for idx,key in enumerate(self.array):
            if key == None:
                return idx
        return False


    def remove(self, idx):
        self.array.pop(idx)


class ContactManager:
    def __init__(self):
        self.contacts = HashTable()


    def loadContacts(self):
        try:
            with open('contacts.json', "r+") as f:
                data = json.load(f)

                for idx,item in enumerate(data):
                    tmpContact = Contact(item["firstName"], item["lastName"], item["number"])
                    self.contacts.add(idx, tmpContact)
        except:
            pass


    def saveContacts(self):
        saveData = []
        for item in self.contacts.array:
            if item != None:
                item = item[0][1]
                saveData.append(item.toJSON())

        with open('contacts.json', "w") as f:
            json.dump(saveData, f)


    def displayAllContacts(self):
        for idx, item in enumerate(self.contacts.array):
            if item != None:
                item = item[-1][1]
                print("Index:", idx, "\n", item.str())


    def addContact(self, firstName, lastName, number):
        tmpContact = Contact(firstName, lastName, number)
        self.contacts.add(self.contacts.last_elem_idx(), tmpContact)


    def deleteContact(self, contact_idx):
        self.contacts.remove(contact_idx)


    def searchContact(self, firstName, lastName):
        for item in self.contacts.array:
            if item != None:
                item = item[0][1]
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


    while True:
        if myContactManager.contacts.is_empty() == True:
            print("There are no contact. You should add.")
            q = "2"
        else:
            q = input("Hi!! here you can select one of the following options:"
                      " "
                      "Press 1 to search, "
                      "press 2 for adding a contact, "
                      "press 3 for deleting a contact, "
                      "press 4 to display all contacts, ")
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
            myContactManager.deleteContact(delete_index)
            try:
                myContactManager.saveContacts()
            except:
                print("Wrong input. exiting...")

        elif q=="4":
            myContactManager.displayAllContacts()

        else:
            print("Wrong input. exiting...")
            break


main()
