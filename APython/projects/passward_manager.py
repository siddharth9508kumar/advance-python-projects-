#passward manager securely store,add,edit,and retrieve passwords using encryption.
#for encryption we will use the cryptography library, which provides a simple and secure way to encrypt and decrypt data.
#we use os library to handle file operations, such as reading and writing the encrypted passwords and the encryption key.
#we use Fernet from the cryptography library to handle encryption and decryption of passwords. Fernet is a symmetric encryption method that ensures the confidentiality of the data.
import os
from cryptography.fernet import Fernet
class PasswordManager:
    def __init__(self, key_file='key.key', password_file='passwords.enc'):
        self.key_file = key_file
        self.password_file = password_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key

    def add_password(self, service, username, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        with open(self.password_file, 'ab') as file:
            file.write(f"{service}:{username}:{encrypted_password.decode()}\n".encode())


    def edit_password(self, service, new_username=None, new_password=None):
        passwords = self.get_passwords()
        if service in passwords:
            username, _ = passwords[service]
            if new_username:
                username = new_username
            if new_password:
                encrypted_password = self.fernet.encrypt(new_password.encode())
                passwords[service] = (username, encrypted_password.decode())
            else:
                passwords[service] = (username, _)
            with open(self.password_file, 'wb') as file:
                for svc, (usr, pwd) in passwords.items():
                    file.write(f"{svc}:{usr}:{pwd}\n".encode())
        else:
            print("Service not found.")
    def get_passwords(self):
        passwords = {}
        if os.path.exists(self.password_file):
            with open(self.password_file, 'rb') as file:
                for line in file:
                    service, username, encrypted_password = line.decode().strip().split(':')
                    decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
                    passwords[service] = (username, decrypted_password)
        return passwords
while True:
    print("Choice the task you want to perform:")
    print("1. Add Password")
    print("2. Edit Password")
    print("3. View Passwords")
    print("4. Exit")
    choice = input("Enter your choice: ")
    manager = PasswordManager()
    if choice == '1':
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        manager.add_password(service, username, password)
    elif choice == '2':
        service = input("Enter service name to edit: ")
        new_username = input("Enter new username (leave blank to keep current): ")
        new_password = input("Enter new password (leave blank to keep current): ")
        manager.edit_password(service, new_username if new_username else None, new_password if new_password else None)
    elif choice == '3':
        passwords = manager.get_passwords()
        for service, (username, password) in passwords.items():
            print(f"Service: {service}, Username: {username}, Password: {password}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")