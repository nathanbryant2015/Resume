from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import yaml

#Sleep for TV Screen to Power on
time.sleep(30) 

# Import yaml config file
# How to call variables print(config['chrome_url02']) or x = config['chrome_url02']
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)

# Specify the path to the ChromeDriver executable
chromedriver_path = config['chrome_driver_path']
Screen_1_Postion_start = config['image_screen_1_start']
Screen_2_Postion_start = config['image_screen_2_start']
Screen_1_Window_Size = config['dashboard_window_1_size']
Screen_2_Window_Size = config['dashboard_window_2_size']

# Configure the Chrome options
options = webdriver.ChromeOptions()

# Set the display for the first browser
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

# Launch the first browser
driver1 = webdriver.Chrome(executable_path=chromedriver_path, options=options)
# Update Window position
options.add_argument(Screen_2_Postion_start)
options.add_argument(Screen_2_Window_Size)
driver2 = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# You can now use the driver1's instance to interact with the browsers

while True:
    driver1.get(config['image_path1'])
    driver2.get(config['image_path2'])
    time.sleep(60 * 60)
