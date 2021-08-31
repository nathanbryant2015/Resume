MasterSiteCreation


#This section is for google drive auth and other modules needed
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

creds = None

SCOPES = ["https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]


if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=8080)
# Save the credentials for the next run.
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

#Call to google API drive.
service = build('drive', 'v3', credentials=creds)


#Input from the User
# root_folder on the google drive. Project folder.
root_folder = input('What is the Google Root Folder ID? You should create one: ')



#Site list to create Google Folder Structure
master_list = open('./sites.txt', 'r').read().split('\n')


master_folders = [
"Configs",
"Packing Slips",
"Quotes",
"Site Survey",
"Site Validation",
"Integration Engineers"
]

site_survey_subfolder = [
"Diagrams",
"Floor Plans",
"Network Topology",
"Survey Pics"
]

survey_pics_subfolder = [
"ER",
"LABs",
"Portables",
"Rooms",
"TRs"
]

site_validation_subfolder = [
"Controller Screenshots",
"Icinga Device List",
"Notes",
"Reports",
"Validation Pics"
]

validation_pics_subfolder = [
"ER",
"LABs",
"Portables",
"Rooms",
"TRs"
]


# This section creates a folder on the drive for each site in the master list. Variables a,b,c,d are for the nested folders.
for site in master_list:
    folder_metadata = {
        'name': site,
        'mimeType': 'application/vnd.google-apps.folder',
        'driveId' : 'XXXXXXXXXXXX',
        'parents' : [root_folder]
    }
    folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
    folder_id = folder.get('id')
    print("Folder Structure Starting for: " + site)

    for i in master_folders:
        folder_metadata = {
            'name': i,
            'mimeType': 'application/vnd.google-apps.folder',
            'driveId' : 'XXXXXXXXXX',
            'parents' : [folder_id]
            }
        folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
        if i == "Site Survey":
            a = folder.get('id')
        if i == "Site Validation":
            c = folder.get('id')
            
    for ii in site_survey_subfolder:
        folder_metadata = {
                'name': ii,
                'mimeType': 'application/vnd.google-apps.folder',
                'driveId' : 'XXXXXXXXXXXXXX',
                'parents' : [a]
                }
        folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
        if ii == "Survey Pics":
            b = folder.get('id')             
    for iii in survey_pics_subfolder:
        folder_metadata = {
                'name': iii,
                'mimeType': 'application/vnd.google-apps.folder',
                'driveId' : 'XXXXXXXXXXXXXXX',
                'parents' : [b]
                }
        folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
                        
    for iiii in site_validation_subfolder:
        folder_metadata = {
            'name': iiii,
            'mimeType': 'application/vnd.google-apps.folder',
            'driveId' : 'XXXXXXXXXXXXXXXXX',
            'parents' : [c]
            }
        folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
        if iiii == "Validation Pics":
            d = folder.get('id')
    for iiiii in survey_pics_subfolder:
        folder_metadata = {
            'name': iiiii,
            'mimeType': 'application/vnd.google-apps.folder',
            'driveId' : 'XXXXXXXXXXXXXXXXX',
            'parents' : [d]
            }
        folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
    print("Finished: " + site)

print("Script completed")
            




