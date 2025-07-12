# Simple Contact Book in Python

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!\n")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print("Contact not found.\n")

def display_contacts():
    if not contacts:
        print("No contacts to display.\n")
    else:
        print("\nAll Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
        print()

def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

