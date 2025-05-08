"""
Objectives
improving the student's skills in reading the CSV files;
using the reader function or the DictReader class.

Scenario
When we buy a new phone, it's necessary to import old contacts.
Why not import them from a CSV file? Look again at the familiar contacts.csv file,
and then design your new phone as follows:
create a class called PhoneContact representing a single contact.

The PhoneContact class should contain the name and phone properties;
create a class called Phone that will store your contacts.

First, implement the method called load_contacts_from_csv,
responsible for reading data from the CSV file into the class property called contacts.

The contacts property should contain a list of PhoneContact objects;
add to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the keyboard,
and then based on it perform a search for all matching contacts (case-insensitive).
If there are no results, print the message: "No contacts found".

Example input:
Search contacts: mother

Example output:
mother (222-555-101)
mother-in-law (222-555-104)

Example input:
Search contacts: 103

Example output:
wife (222-555-103)
"""

import csv


class PhoneContact:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def contact(self):
        return self._name + ' ' + '(' + self._phone + ')'

    @contact.setter
    def contact(self, value):
        self.contact = value


def load_contacts_from_csv():
    """
    Task:
    implement the method called load_contacts_from_csv,
    responsible for reading data from the CSV file into the class property called contacts
    The contacts property should contain a list of PhoneContact objects
    """
    with open('contacts.csv', newline='') as csvfile:
        """
        csv.DictReader() method with parameters file and fieldnames
        """
        fieldnames = ['Name', 'Phone']
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        contacts = []
        for row in reader:
            pc = PhoneContact(row['Name'], row['Phone'])
            contacts.append(pc.contact)
        print(contacts[1:])
        return contacts


class Phone:
    contacts = load_contacts_from_csv()

    def search_contacts(self):
        """
        Task:
        search_contacts, which accepts any phrase entered by the user from the keyboard,
        and then based on it perform a search for all matching contacts (case-insensitive).
        If there are no results, print the message: "No contacts found".
        """
        indexes = []
        search_input = (input('Search contacts: ')).lower()
        list_of_contacts = Phone.contacts
        for contact in list_of_contacts:
            index = contact.find(search_input)
            if index >= 0:
                contanct_index = list_of_contacts.index(contact)
                print(list_of_contacts[contanct_index])
            else:
                indexes.append(index)
                if len(indexes) == len(list_of_contacts):
                    print('Contact not found')


if __name__ == "__main__":
    Phone().search_contacts()


"""
['mother (222-555-101)', 'father (222-555-102)', 'wife (222-555-103)', 'mother-in-law (222-555-104)']
Search contacts: father
father (222-555-102)

Search contacts: brother
Contact not found

Search contacts: 555
mother (222-555-101)
father (222-555-102)
wife (222-555-103)
mother-in-law (222-555-104)
"""
