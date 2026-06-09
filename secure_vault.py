from cryptography.fernet import Fernet
import os

def generate_and_save_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 New key generated and saved as 'secret.key'.")

def load_key():
    if not os.path.exists("secret.key"):
        raise FileNotFoundError("Error: 'secret.key' not found. Generate a key first.")
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"🔒 '{filename}' has been successfully encrypted!")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"🔓 '{filename}' has been successfully decrypted!")

if __name__ == "__main__":
    print("\n--- Welcome to your Personal Crypto Vault ---")
    print("1. Generate a new encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Choose an option (1-3): ")
    if choice == "1":
        generate_and_save_key()
    elif choice in ["2", "3"]:
        target_file = input("Enter the exact filename (e.g., secret_notes.txt): ")
        try:
            if choice == "2":
                encrypt_file(target_file)
            else:
                decrypt_file(target_file)
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    else:
        print("Invalid choice!")