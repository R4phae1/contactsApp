import json

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data.str())
            temp = temp.next


class ContactManager:
    def __init__(self):
        self.contacts = LinkedList()


    def loadContacts(self):
        try:
            with open('contacts.json', "r+") as f:
                data = json.load(f)

                tmpNode = None

                for idx,item in enumerate(data):
                    tmpContact = Contact(item["firstName"], item["lastName"], item["number"])
                    n = Node(tmpContact)

                    if idx == 0:
                        self.contacts.head = n
                        tmpNode = n
                        continue

                    tmpNode.next = n
                    tmpNode = n
        except FileNotFoundError:
            with open('contacts.json', 'w') as f:
                pass
        except:
            self.contacts = LinkedList()


    def saveContacts(self):
        saveData = []

        temp = self.contacts.head
        while temp:
            item = temp.data
            saveData.append(item.toJSON())
            temp = temp.next

        with open('contacts.json', "w") as f:
            json.dump(saveData, f)


    def displayAllContacts(self):
        temp = self.contacts.head
        idx = 0
        while temp:
            item = temp.data

            print("Index:", idx, "\n", item.str())

            idx += 1
            temp = temp.next


    def addContact(self, firstName, lastName, number):
        tmpContact = Contact(firstName, lastName, number)
        n = Node(tmpContact)

        if self.contacts.head == None:
            self.contacts.head = n
        else:
            temp = self.contacts.head

            while temp:
                if temp.next == None:
                    temp.next = n
                    break
                temp = temp.next


    def deleteContact(self, contact_idx):
        # If linked list is empty
        if self.contacts.head == None:
            return

        # Store head node
        temp = self.contacts.head

        # If head needs to be removed
        if contact_idx == 0:
            self.contacts.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(contact_idx -1 ):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next


    def searchContact(self, firstName, lastName):
        temp = self.contacts.head
        while temp:
            item = temp.data
            temp = temp.next

            if item.firstName == firstName and item.lastName == lastName:
                print(item.str())
                break


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
        if myContactManager.contacts.head == None:
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

        elif q=="4":
            myContactManager.displayAllContacts()

        elif q == "3":
            myContactManager.displayAllContacts()
            delete_index = int(input("Select index for deleting contact: "))
            myContactManager.deleteContact(delete_index)
            try:
                myContactManager.saveContacts()
            except:
                print("Wrong index input. exiting...")

        else:
            print("Wrong input. exiting...")
            break




main()
