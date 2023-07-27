from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml

#Sleep for TV Screen to Power on
time.sleep(30) 


#import yaml config file
#How to call variables print(config['chrome_url02']) or x = config['chrome_url02']
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)

#Variables
email = config['google_user']
password = config['google_pw']
chromedriver_path = config['chrome_driver_path']
Screen_1_Postion_start = config['dashboard_screen_1_start']
Screen_1_Window_Size = config['dashboard_window_1_size']

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

#Open chrome and go to google_login
driver1.get(config['google_login'])
#sleep to load page
time.sleep(3)
#Find field to input email
email_field = driver1.find_element(By.CSS_SELECTOR, 'input[type="email"]')
email_field.send_keys(email)
#Click the next button
next_button = driver1.find_element(By.CSS_SELECTOR, "#identifierNext")
next_button.click()
#sleep to load page
time.sleep(3)
#Find and enter password
password_field = driver1.find_element(By.CSS_SELECTOR, 'input[type="password"]')
password_field.send_keys(password)
#click login
login_button = driver1.find_element(By.CSS_SELECTOR, "#passwordNext")
login_button.click()
time.sleep(3)


# You can now use the driver1's instance to interact with the browsers
while True:
    driver1.get(config['chrome_url01'])
    time.sleep(60 * 60)