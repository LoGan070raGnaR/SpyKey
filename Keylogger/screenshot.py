from PIL import ImageGrab

# Function to capture screenshot
def capture_screenshot(file_path):
    screenshot = ImageGrab.grab()
    screenshot.save(file_path + "/f_screenshot.png")
