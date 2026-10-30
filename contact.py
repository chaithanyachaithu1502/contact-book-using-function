##contact

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    # Convert to lowercase internally to prevent case-sensitive duplicates
    if name.lower() in contacts:
        print("Contact already exists!")
    else:
        contacts[name.lower()] = {"display_name": name, "phone": phone}
        print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name to search: ").strip().lower()

    if name in contacts:
        print(f"Name: {contacts[name]['display_name']}")
        print(f"Phone Number: {contacts[name]['phone']}")
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter contact name to update: ").strip().lower()

    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        contacts[name]["phone"] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts():
    if contacts:
        print("\n--- Saved Contacts ---")
        for info in contacts.values():
            print(f"Name: {info['display_name']} | Phone: {info['phone']}")
    else:
        print("No contacts available!")

def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact\n2. Search Contact\n3. Update Contact")
        print("4. Delete Contact\n5. View All Contacts\n6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Thank you for using Contact Management System!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
