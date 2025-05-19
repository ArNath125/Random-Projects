import os
import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

#generate key from password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

#encrypt files
def encrypt_files(filenames, key):
    f = Fernet(key)
    for filename in filenames:
        with open(filename, 'rb') as file:
            data = file.read()
        encrypted_data = f.encrypt(data)
        with open(filename+".enc", 'wb') as file:
            file.write(encrypted_data)

#decrypt files
def decrypt_files(filenames, key):
    f = Fernet(key)
    for filename in filenames:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        output_file = os.path.join(os.path.dirname(filename),"decrypted_" + filename.split("/")[-1].replace(".enc", ""))
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

#generate salt
def generate_salt():
    salt = os.urandom(16)
    with open("salt.key","wb") as sf:
        sf.write(salt)
    return salt

#get key
def get_key(password):
    with open("salt.key", "rb") as sf:
        salt = sf.read()
    key = generate_key(password, salt)
    return key

#main function
def main():
    choice = input("Do you want to encrypt or decrypt files? (e/d): ").lower()
    file_input = input("Enter the file name(s) (comma separated): ").split(",")
    password = getpass.getpass("Enter the password: ")

    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    all_files = os.listdir(script_dir)

    salt_file = "salt.key"

    if choice == "e":
        generate_salt()
        file_encrypt = [os.path.join(script_dir, f) for f in file_input if f in all_files and not f.endswith(".enc") and not f.startswith("decrypted_")]
        if not file_encrypt:
            print("No valid files to encrypt.")
            return
        encrypt_files(file_encrypt, get_key(password))
        print("Encryption complete.")
    elif choice == "d":
        file_decrypt = [os.path.join(script_dir, f) for f in file_input if f in all_files and f.endswith(".enc")]
        if not file_decrypt:
            print("No valid files to decrypt.")
            return
        decrypt_files(file_decrypt, get_key(password))
        print("Decryption complete.")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
# This code encrypts and decrypts files using a password-based key derivation function (PBKDF2) and the Fernet symmetric encryption algorithm.