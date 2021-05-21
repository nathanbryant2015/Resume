#google sheets modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time



#Below authenticates you to the google Drive/spreadsheets, the creds.json must be in the same file as script. See XXXXXXXXXXXXXX to get a key.
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


#Main google sheet that will be copied
main_page = 'Google Link here'
sh = client.open_by_url(main_page)
sh = sh.worksheet("WSName")
print(sh)

#List of sheets to receive WSName
google_sheet_list = [list here]

for site in google_sheet_list:
    sh.copy_to(site)
    print(site + ' complete')
    time.sleep(5)
