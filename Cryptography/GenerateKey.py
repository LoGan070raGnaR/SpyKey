from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Open a file to store the encryption key
file = open("encryption_key.txt", 'wb')

# Write the key to the file
file.write(key)

# Close the file
file.close()
