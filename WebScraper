#Web scrape modules
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import html5lib


#google sheets modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from gspread_dataframe import set_with_dataframe
import gspread_dataframe as gd


#data frame module
import pandas as pd

#Password module
from getpass import getpass

#Below is just a script banner.
print('***********************************************************')
print('*      WARNING!                                           *')
print('*      ----------------------------------------------     *')
print('*      This script is to be logged in to or used          *')
print('*      only by specifically authorized personnel;         *')
print('*                                                         *')
print('*      Any unauthorized use of this script                *')
print('*      is unlawful,and may be subject to civil            *')
print('*      and/or criminal penalties;                         *')
print('*                                                         *')
print('*      Any use of this script may be logged               *')
print('*      or monitored without further notice,               *')
print('*      and the resulting logs may be used as              *')
print('*      evidence in a court of law.                        *')
print('*                                                         *')
print('*      Contact XXXXXXXXXXXXXXXXXXXX for access            *')
print('*                                                         *')
print('***********************************************************')
print('                                                           ')
print('#######     Created by XXXXXXXXXXXXXXXXXXXXXXXX     #######')
print('                                                           ')
print('                                                           ')
print('                    Web Scrape Script                      ')
print('                                                           ')
print('                                                           ')


#Below authenticates you to the Google Drive/spreadsheets, the creds.json must be in the same file as script. See XXXXXXXXX to get a key.
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


#Variable input from User
print("")
print("")
site_code = input("What is the site code? :")
user_name = input("What is your AD Username? :")
password = getpass()
link = input("What is the google link to the IG? (any Link): ")


#Scrape variables
page = 'http://websitename.com'
page_url = page + site_code
login_page = 'https://webpage2.com/login'
wifi_psk_page = 'http://website3.com/psk'


#Web browser, Headless setup
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(r'C:\Scripts\WebScraper\chromedriver.exe', options=option)



#Login to website
driver.get(login_page)
driver.find_element_by_name("Username").send_keys(user_name)
driver.find_element_by_name("Password").send_keys(password)
driver.find_element_by_name("Command").click()
driver.find_element_by_name("Command").click()


#Site page
driver.get(page_url)


#scrape tool
soup = bs(driver.page_source, "lxml")

print("")
print("")
print("")
print("[Status] Starting Web Scrape From XXXXXXX")
print("")
print("")
#--------------------------------Scrape Info. and update Cell on Google drive.
try:
    school_name = soup.find('h2').getText()
    wks_name = 'Formulas'
    sheet = client.open_by_url(link).worksheet(wks_name)
    sheet.update('B3', school_name)
    print("[INFO] Site Name Scraped and Updated on Cover Page")
    print("")
    print("")
except:
    print('*************Failed Site name update***************************************')
    print("")
    print("")
    pass

#--------------------------------General Info.
#scrape
try:
    general_information_data = soup.find_all('td')
    print('[INFO] Scraped General Info')
    print("")
    print("")
except:
    print('*************Failed General Info Scrape***************************************')
    print("")
    print("")
    pass
#--------------------------------Server Info.
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('ServerInfo')
    soup = bs(driver.page_source, "lxml")
    server_data = soup.find_all('td')
    print('[INFO] Scraped Server Info')
    print("")
    print("")
except:
    print('*************Failed Server Info Scrape***************************************')
    print("")
    print("")
    pass
#--------------------------------Asset List.
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('AssetList')
    soup = bs(driver.page_source, "lxml")
    asset_list = soup.find_all('td')
    print('[INFO] Scraped Asset List')
    print("")
    print("")
except:
    print('*************Failed Asset Scrape***************************************')
    print("")
    print("")
    pass
#--------------------------------IP SUBNET LIST.
#change page and re-scrape.
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('IPSubnetList')
    soup = bs(driver.page_source, "lxml")
    ip_subnet_table = soup.find('table', id='IPSubnetList')
    print('[INFO] Scraped IP Subnet List')
    print("")
    print("")
except:
    print('*************Failed IP Subnet List Scrape***************************************')
    print("")
    print("")
    pass
#--------------------------------DeviceDiscoveryList.
#change page and re-scrape.
#select all makes and clicks all macs
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('DeviceDiscoveryList')
    driver.find_element_by_name("ShowAllAddresses").click()
    drop_down = Select(driver.find_element_by_name('MakeFilter'))
    drop_down.select_by_value('**ALL')
    soup = bs(driver.page_source, "lxml")
    device_discovery_list = soup.find('table', id='DeviceDiscoveryList')
    print('[INFO] Scraped Device Discovery List')
    print("")
    print("")
except:
    print('*************Failed Device DiscoveryList Scrape***************************************')
    print("")
    print("")
    pass
#--------------------------------Technical POC.
#change page and re-scrape.
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('TechPOCList')
    soup = bs(driver.page_source, "lxml")
    tech_poc = soup.find_all('td')
    print('[INFO] Scraped Techical POC')
    print("")
    print("")
except:
    print('*************Failed Technical POC Scrape***************************************')
    print("")
    print("")
    pass
#-------------------------------Recent Help Desk Tickets.
#change page and re-scrape.
try:
    drop_down = Select(driver.find_element_by_name('Panel'))
    drop_down.select_by_value('SiteHDTickets')
    driver.find_element_by_css_selector("input[type='radio'][value='365']").click()
    soup = bs(driver.page_source, "lxml")
    recent_help_desk_tickets = soup.find_all('td')
    print('[INFO] Scraped Recent Helpdesk Tickets')
    print("")
    print("")
except:
    print('*************Failed Recent Help Desk Scrape***************************************')
    print("")
    print("")
    pass
#----------------------------WIFI PSK
try:
    driver.get(wifi_psk_page)
    soup = bs(driver.page_source, "lxml")
    wifi_psk = soup.find_all()
    print('[INFO] Scraped WIFI PSK')
    print("")
    print("")
except:
    print('*************Failed WIFI PSK Scrape***************************************')
    print("")
    print("")
    pass

###Pandas convert scrape to data frame

print('[Status] WebScrape Complete, Converting to Data Frames')
print("")
print("")
try:
    general_info_df = pd.read_html(str(general_information_data))[1]
    print('[INFO] Converting General Info to Data Frame')
    print("")
    print("")
except IndexError:
    general_info_df = pd.read_html(str(general_information_data))[0]
    print('[INFO] Converting General Info to Data Frame')
    print("")
    print("")
except:
    print(" *************Converting General info to dataframe failed*************")
    print("")
    print("")
    pass
        

try:
    ip_subnet_table_df = pd.read_html(str(ip_subnet_table))[1]
    print('[INFO] Converting IP Subnet Table to Data Frame')
    print("")
    print("")
except IndexError:
    ip_subnet_table_df = pd.read_html(str(ip_subnet_table))[0]
    print('[INFO] Converting IP Subnet Table to Data Frame')
    print("")
    print("")
except:
    print("*************Converting IP Subnet Table to dataframe failed*************")
    print("")
    print("")
    pass
  

try:
    device_discovery_list_df = pd.read_html(str(device_discovery_list))[0]
    print('[INFO] Converting Device Discovery List to Data Frame')
    print("")
    print("")
except IndexError:
    device_discovery_list_df = pd.read_html(str(device_discovery_list))[1]
    print('[INFO] Converting Device Discovery List to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Device Discovery List to dataframe failed*************")
    print("")
    print("")
    pass
    

try:
    server_data_df = pd.read_html(str(server_data))[1]
    print('[INFO] Converting Server Data to Data Frame')
    print("")
    print("")
except IndexError:
    server_data_df = pd.read_html(str(server_data))[0]
    print('[INFO] Converting Server Data to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Server Data to dataframe failed*************")
    print("")
    print("")
    pass


try:
    tech_poc_df = pd.read_html(str(tech_poc))[1]
    print('[INFO] Converting Technical POC to Data Frame')
    print("")
    print("")
except IndexError:
    tech_poc_df = pd.read_html(str(tech_poc))[0]
    print('[INFO] Converting Technical POC to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Technical POC to dataframe failed*************")
    print("")
    print("")
    pass


try:
    asset_list_df = pd.read_html(str(asset_list))[1]
    print('[INFO] Converting Asset List to Data Frame')
    print("")
    print("")
except IndexError:
    asset_list_df = pd.read_html(str(asset_list))[0]
    print('[INFO] Converting Asset List to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Asset List to dataframe failed*************")
    print("")
    print("")
    pass


try:
    recent_help_desk_tickets_df = pd.read_html(str(recent_help_desk_tickets))[1]
    print('[INFO] Converting Recent Help Desk Tickets to Data Frame')
    print("")
    print("")
except IndexError:
    recent_help_desk_tickets_df = pd.read_html(str(recent_help_desk_tickets))[0]
    print('[INFO] Converting Recent Help Desk Tickets to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Recent Help Desk Tickets to dataframe failed*************")
    print("")
    print("")
    pass
    

try:
    closed_help_desk_tickets_df = pd.read_html(str(recent_help_desk_tickets))[3]
    print('[INFO] Converting Closed Help Desk Tickets to Data Frame')
    print("")
    print("")
except IndexError:
    closed_help_desk_tickets_df = pd.read_html(str(recent_help_desk_tickets))[0]
    print('[INFO] Converting Closed Help Desk Tickets to Data Frame')
    print("")
    print("")
except:
    print("*************Converting Closed Help Desk Tickets to dataframe failed*************")
    print("")
    print("")
    pass

    
try:    
    wifi_psk_df = pd.read_html(str(wifi_psk))[0]
    print('[INFO] Converting WIFI PSK to Data Frame')
    print("")
    print("")
except:
    print("*************Converting WIFI PSK to dataframe failed*************")
    print("")
    print("")
    pass

print('[Status] All Data Convereted to Data Frame, Starting Upload to Google Sheet')
print("")
print("")




#pandas df to google sheets df, upload to sheets
#--------------------------------General Info.
try:
    wks_name = 'general_info_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, general_info_df)
    print('[INFO] Uploaded to general_info_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------Server Information.
try:
    wks_name = 'server_data_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, server_data_df)
    print('[INFO] Uploaded to server_data_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------Asset List.
try:
    wks_name = 'asset_list_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, asset_list_df)
    print('[INFO] Uploaded to asset_list_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------IP SUBNET LIST.
try:
    wks_name = 'ip_subnet_table_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, ip_subnet_table_df)
    print('[INFO] Uploaded to ip_subnet_table_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------DeviceDiscoveryList.
try:
    wks_name = 'device_discovery_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, device_discovery_list_df)
    print('[INFO] Uploaded to device_discovery_list_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------Technical POC.
try:
    wks_name = 'tech_poc_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, tech_poc_df)
    print('[INFO] Uploaded to tech_poc_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------Recent Help Desk Tickets.
try:
    wks_name = 'recent_help_desk_tickets_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, recent_help_desk_tickets_df)
    print('[INFO] Uploaded to recent_help_desk_tickets_df')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------Recent Closed Help Desk Tickets.
try:
    wks_name = 'closed_help_desk_tickets_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, closed_help_desk_tickets_df)
    print('[INFO] Uploaded to closed_help_desk_tickets_df')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass
#pandas df to google sheets df, upload to sheets
#--------------------------------WIFI PSK.
try:
    wks_name = 'wifi_psk_df'
    sheet = client.open_by_url(link).worksheet(wks_name)
    gd.set_with_dataframe(sheet, wifi_psk_df)
    print('[INFO] Uploaded to wifi_psk_df sheet')
    print("")
    print("")
except:
    print("***********" + wks_name + " Failed to Upload to Sheet" + "**************")
    print("")
    print("")
    pass

print('[Status] Done!)
print("")
print("")

