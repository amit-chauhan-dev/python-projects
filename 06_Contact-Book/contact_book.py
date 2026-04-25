def load_contacts():
    contacts = {}
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}, {phone}\n")
        
def show_contacts(contacts):
    if not contacts:
        print("No contacts found ")
    else:
        print("\n Contact List: ")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contacts saved ")

def search_contact(contacts):
    name = input("Enter name search: ")
    if name in contacts:
        print(f"Found {name} : {contacts[name]}")
    else:
        print("Contact not found ")
    
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted ")
    else:
        print("Contact not found! ")
    
# Main program 
Contacts = load_contacts()

while True:
    print("\n Contact Book Menu")
    print("1. View Contacts")
    print("2. Add Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        show_contacts(Contacts)
    elif choice == "2":
        add_contact(Contacts)
        save_contacts(Contacts)
    elif choice == "3":
        search_contact(Contacts)
    elif choice == "4":
        delete_contact(Contacts)
        save_contacts(Contacts)
    elif choice == "5":
        save_contacts(Contacts)
        print("Goodbye")
        break
    else:
        print("Invalid choice! try again.")