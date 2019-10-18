

import json


class Contact:

    def __init__(self, firstName="", lastName="", number=""):
        self.fullName = firstName + " " + lastName
        self.number = number
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"First name: {self.firstName}\nLast name: {self.lastName}\nPhone number: {self.number}\n"

    def save_contact(self):
        with open('./contacts.json', "r") as f:
            x = json.load(f)
            x.append(Contact.contact_to_dict(self))

        with open('./contacts.json', "w") as f:
            json.dump(x, f)

    def delete_contact(self):
        #updated_list = []
        with open('./contacts.json', "r") as f:
            x = list(json.load(f))
            for indexs, each in enumerate(x):
                if each["firstName"] == self.firstName and each["lastName"] == self.lastName:
                    del(x[indexs])

        with open('./contacts.json', "w") as f:
            json.dump(x, f)

    @staticmethod
    def get_all_contacts():
        with open('./contacts.json', "r+") as f:
            data = list(json.load(f))
        return data


    @staticmethod
    def search_contact(firstName, lastName):
        Contact.get_all_contacts()
        for each in Contact.get_all_contacts():
            if each["firstName"] == firstName and each["lastName"] == lastName:
                return each
        return 0

    @staticmethod
    def contact_to_dict(contact_obj):
        return {"firstName": contact_obj.firstName, "lastName": contact_obj.lastName, "number": contact_obj.number}


def input_full_name():
    firstName = input("Please enter the first name: ")
    lastName = input("Please enter the last name: ")
    return firstName, lastName

def main():
    print("Welcome to phone book app.")
    while True:
        print("You may select one of the following options:")

        choice = int(input("""
        1. Create contact
        2. Show contacts
        3. Search contact
        4. Edit contact
        5. Delete contact
        0. Exit
        """))
        if choice == 0:
            exit()
        elif choice == 1:
            firstName, lastName = input_full_name()
            number = input("Please enter the number: ")
            newContact=Contact(firstName=firstName, lastName=lastName, number=number)
            newContact.save_contact()
        elif choice == 2:
            for each in Contact.get_all_contacts():
                print(Contact(each["firstName"], each["lastName"], each["number"]))
        elif choice == 3:
            firstName, lastName = input_full_name()
            founded = Contact.search_contact(firstName, lastName)
            if founded == 0:
                print("no such contact in your list")
            else:
                fcontact = Contact(founded["firstName"], founded["lastName"], founded["number"])
                print(fcontact)
        elif choice == 4:
            firstName, lastName = input_full_name()
            founded = Contact.search_contact(firstName, lastName)
            if founded == 0:
                print("no such contact in your list")
            else:
                fcontact = Contact(founded["firstName"], founded["lastName"], founded["number"])
                fcontact.delete_contact()
                new_firstName = fcontact.firstName
                new_lastName = fcontact.lastName
                new_number = fcontact.number

                print("What to edit:")
                edit_field = int(input("""
                    1. First name
                    2. Last name
                    3. Number
                    """))
                if edit_field == 1:
                    new_firstName = input("Please enter new first name")
                elif edit_field == 2:
                    new_lastName = input("Please enter new last name")
                else:
                    new_number = input("Please enter new number")

            editedcontact = Contact(new_firstName, new_lastName, new_number)
            editedcontact.save_contact()

        elif choice == 5:
            firstName, lastName = input_full_name()
            deletedcontact = Contact(firstName=firstName, lastName=lastName)
            deletedcontact.delete_contact()
