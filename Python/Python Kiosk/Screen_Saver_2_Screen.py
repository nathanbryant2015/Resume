import os
from selenium import webdriver
import yaml
import time
import threading

#Sleep for TV Screen to Power on
time.sleep(30) 

# Load configuration from YAML file
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)

# Variables for screen 1
driver_path_screen1 = config['chrome_driver_path']
photo_directory_screen1 = config['photo_directory_screen1']
screen1_start_position = config['screen_saver_screen_1_start']
screen1_window_size = config['screen_saver_window_1_size']

# Variables for screen 2
driver_path_screen2 = config['chrome_driver_path']
photo_directory_screen2 = config['photo_directory_screen2']
screen2_start_position = config['screen_saver_screen_2_start']
screen2_window_size = config['screen_saver_window_2_size']

# Configure the Chrome options for screen 1
options_screen1 = webdriver.ChromeOptions()
options_screen1.add_argument("--start-maximized")
options_screen1.add_experimental_option("useAutomationExtension", False)
options_screen1.add_experimental_option("excludeSwitches", ["enable-automation"])
options_screen1.add_argument("--kiosk")
options_screen1.add_argument("--disable-infobars")
options_screen1.add_argument("--disable-notifications")
options_screen1.add_argument("--disable-popup-blocking")
options_screen1.add_argument("--ignore-certificate-errors")
options_screen1.add_argument(screen1_start_position)
options_screen1.add_argument(screen1_window_size)

# Configure the Chrome options for screen 2
options_screen2 = webdriver.ChromeOptions()
options_screen2.add_argument("--start-maximized")
options_screen2.add_experimental_option("useAutomationExtension", False)
options_screen2.add_experimental_option("excludeSwitches", ["enable-automation"])
options_screen2.add_argument("--kiosk")
options_screen2.add_argument("--disable-infobars")
options_screen2.add_argument("--disable-notifications")
options_screen2.add_argument("--disable-popup-blocking")
options_screen2.add_argument("--ignore-certificate-errors")
options_screen2.add_argument(screen2_start_position)
options_screen2.add_argument(screen2_window_size)

def display_images(driver, photo_directory):
    # Get a list of all the .png files
    image_files = [f for f in os.listdir(photo_directory) if f.endswith('.png')]

    start_time = time.time()

    # Loop through the image files for 2 hours
    while time.time() - start_time < 2 * 60 * 60:
        for image_file in image_files:
            # Construct the full path to the image file
            image_path = os.path.join(photo_directory, image_file)

            # Open the image file in the browser
            driver.get('file://' + image_path)
            time.sleep(5)

# Create and start threads for each screen
thread_screen1 = threading.Thread(target=display_images, args=(webdriver.Chrome(executable_path=driver_path_screen1, options=options_screen1), photo_directory_screen1))
thread_screen2 = threading.Thread(target=display_images, args=(webdriver.Chrome(executable_path=driver_path_screen2, options=options_screen2), photo_directory_screen2))

thread_screen1.start()
thread_screen2.start()

# Wait for threads to finish
thread_screen1.join()
thread_screen2.join()
