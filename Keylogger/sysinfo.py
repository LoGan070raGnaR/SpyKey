import platform
import socket
from requests import get

# Function to retrieve computer information
def computer_information(file_path):
    with open(file_path + "/f_sysinfo.txt", "a") as f:
        # Get the hostname of the computer
        hostname = socket.gethostname()
        # Get the local IP address of the computer
        IPAddr = socket.gethostbyname(hostname)
        
        try:
            # Get the public IP address of the computer using an API
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)\n")
        
        # Write the processor information to the file
        f.write("Processor: " + (platform.processor()) + '\n')
        
        # Write the system information to the file
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        
        # Write the machine information to the file
        f.write("Machine: " + platform.machine() + "\n")
        
        # Write the hostname to the file
        f.write("Hostname: " + hostname + "\n")
        
        # Write the private IP address to the file
        f.write("Private IP Address: " + IPAddr + "\n")
