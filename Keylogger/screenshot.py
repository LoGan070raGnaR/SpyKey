from PIL import ImageGrab  # Import the module for capturing screenshots

# Function to capture screenshot
def capture_screenshot(file_path):
    screenshot = ImageGrab.grab()  # Capture the screenshot using the ImageGrab module
    screenshot.save(file_path + "/f_screenshot.png")  # Save the screenshot as a PNG file
