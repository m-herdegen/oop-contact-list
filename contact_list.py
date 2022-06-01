# Let's create a class for creating contact lists. Each contact list should store its `contacts` as a list of dictionaries, containing name and phone number. The list should be sorted by the contacts' name. The contact list should also have a `name` that distinguishes it, e.g. "School Friends", "Extended Family", or "Work Buddies". 
# The contact list should have 3 instance methods:
# - `add_contact({})` should add a new contact to the list, while keeping the list sorted
# - `remove_contact('Alice')` should remove a contact from the list by name.
# - `find_shared_contacts(ContactList)` should accept another contact list as an argument, and then return a new list of dictionaries to indicate all the contacts that appear in both lists (exact same name and phone number).

class ContactList():

    def __init__(self, name, contacts):
        self.name = name 
        self.contacts = contacts 
    
    def __str__(self):
        return(f"{self.name}:\n{self.contacts}")

    def add_contact(self, new_contact):
        self.contacts.append(new_contact)
        self.contacts = sorted(self.contacts, key=lambda d: d['name'])

    def remove_contact(self, contact_name):
        for i,element in enumerate(self.contacts):
            print(i, ' ', element)
            if contact_name in element.values():
                print('found')
                self.contacts.pop(i)

    def find_shared_contacts(self, list_name):
        ans = []
        for element in self.contacts:
            for item in list_name.contacts:
                if element == item:
                    ans.append(element)
        return ans


# ```python
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
# print(my_friends_list)
my_friends_list.add_contact({'name': 'Talulah', 'number': '555-4444'})
my_friends_list.add_contact({'name': 'Ally', 'number': '555-4444'})
print(my_friends_list)
# my_friends_list.remove_contact('Alice')
# print('REMOVED\n',my_friends_list,'\n\n\n')
my_work_buddies = ContactList('Work Buddies', work_buddies)
# print(my_work_buddies)
print('\n\nMATCH')

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]
