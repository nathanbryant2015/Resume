import os
from selenium import webdriver
import yaml
import time

#Sleep for TV Screen to Power on
time.sleep(30) 

# Load configuration from YAML file
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)

# Variables
driver_path = config['chrome_driver_path']
photo_directory_screen1 = config['photo_directory_screen1']
Screen_1_Postion_start = config['screen_saver_screen_1_start']
Screen_1_Window_Size = config['screen_saver_window_1_size']

# Configure the Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--kiosk")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument(Screen_1_Postion_start)
options.add_argument(Screen_1_Window_Size)

while True:
    # Initialize the Chrome driver
    driver1 = webdriver.Chrome(executable_path=driver_path, options=options)

    # Get a list of all the .png files in the directory
    image_files = [f for f in os.listdir(photo_directory_screen1) if f.endswith('.png')]

    start_time = time.time()

    # Loop through the image files for 2 hours
    while time.time() - start_time < 2 * 60 * 60:
        for image_file in image_files:
            # Construct the full path to the image file
            image_path = os.path.join(photo_directory_screen1, image_file)

            # Open the image file in the browser
            driver1.get('file://' + image_path)
            time.sleep(5)

    # Close the driver
    driver1.quit()
