import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f'Contact "{name}" added.')

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    """Search for contacts by name or phone number."""
    search = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search.lower() in contact['name'].lower() or search in contact['phone']]
    
    if not results:
        print("No contacts found.")
    else:
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)

def update_contact(contacts):
    """Update a contact's details."""
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current value):")
            contact['name'] = input(f"Name [{contact['name']}]: ") or contact['name']
            contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
            print(f'Contact "{contact["name"]}" updated.')
            return
    print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            print(f'Contact "{name}" deleted.')
            return
    print("Contact not found.")

def main():
    """Main function to run the contact list application."""
    contacts = load_contacts()
    while True:
        print("\nContact List Application")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
