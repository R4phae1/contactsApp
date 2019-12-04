import json

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)




class ContactManager:
    def __init__(self):
        self.contacts = Tree()


    def loadContacts(self):
        try:
            with open('contacts.json', "r+") as f:
                data = json.load(f)
                lastNode = None

                for idx,item in enumerate(data):
                    tmpContact = Contact(item["firstName"], item["lastName"], item["number"])
                    self.contacts.add(tmpContact)
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
        if myContactManager.contacts.root == None:
            print("There are no contact. You should add.")
            q = "2"
        else:
            q = input("Hi!! here you can select one of the following options: \n"
                      "\n"
                      "Press 1 to search, \n"
                      "press 2 for adding a contact, \n"
                      "press 3 for deleting a contact, \n"
                      "press 4 to display all contacts, \n")
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
