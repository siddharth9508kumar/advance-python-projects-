#2.Contact Book Develop a contact book that can save, edit, and search contacts. 
#Handle errors such as duplicate entries, empty fields, and wrong phone number format. 
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def save_contact(self, name, phone):
        if not name:
            raise ValueError("Contact name cannot be empty")
        if not phone:
            raise ValueError("Phone number cannot be empty")
        if name in self.contacts:
            raise ValueError("Contact already exists")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be a 10-digit number")
        self.contacts[name] = phone
    def edit_contact(self, name, new_phone):
        if name not in self.contacts:
            raise ValueError("Contact does not exist")
        if not new_phone:
            raise ValueError("Phone number cannot be empty")
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("Phone number must be a 10-digit number")
        self.contacts[name] = new_phone
    def search_contact(self, name):
        return self.contacts.get(name, None)
# test the contact book
if __name__ == "__main__":
    contact_book = ContactBook()
    try:
        print("Saving contact...")
        n1 = input("Enter contact name: ")
        p1 = input("Enter phone number: ")
        contact_book.save_contact(n1, p1)
        print("Contact saved successfully.")
        print("Editing contact...")
        new_p1 = input("Enter new phone number for {}: ".format(n1))
        contact_book.edit_contact(n1, new_p1)
        print("Contact updated successfully.")
        print("Searching for contact...")
        search_name = input("Enter contact name to search: ")
        phone = contact_book.search_contact(search_name)
        if phone:
            print(f"Contact found: Name: {search_name}, Phone: {phone}")
        else:
            print("Contact not found.")
    except ValueError as e:
        print(e)
