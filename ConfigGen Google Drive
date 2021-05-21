#This section is for google sheets auth and other modules needed
import gspread
import pandas as pd
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build


#This section is for google drive auth and other modules needed
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload


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
print('                Configuration Generator                    ')
print('                                                           ')
print('                                                           ')



#Below authenticates you to the Google Drive/spreadsheets, the creds.json must be in the same file as script. See XXXXXXXXXX to get a key.
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
get_gdrive_service = build('drive', 'v3', credentials=creds)
service = get_gdrive_service


#Below will open up the specific IG needed.
link = input("""What is the google IG link (paste link)? This can be any URL associated to the IG: """"")
print('')
print('')


#User input that determines which RTR config to use. See RTR for loop below.
new_old_vlan = input("""Does this site have the "NEW" or "OLD" Vlan Scheme? Case sensitive: """ )
print('')
print('')


##Generates folder structure on the local machine to save the configuration files.
site_code = input("What is the site code? This creates a folder for the files: ")
school_folders = "C:\\Scripts\\ConfigGen\\Schools\\"
home_folder = school_folders + site_code + ("\\")
template_path = "C:\\Scripts\\ConfigGen\\Templates"
if not os.path.exists(school_folders + site_code ):
    os.mkdir(school_folders + site_code)


#This will open up the specific google spreadsheet, and pull down the data from the configuration tab.
sheet = client.open_by_url(link)
worksheet = sheet.worksheet("configurations")
parameter = worksheet.get_all_records()
df = pd.DataFrame(parameter)
switch_data = df.to_dict('records')


#This creates the jinja2 environment and pulls in the templates to merge with the variables
file_loader = FileSystemLoader(template_path)
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=template_path))

#Tempatles for devices per model
classroom = "ClassroomC12-AiO-Rv.2.txt"
classroomenv = env.get_template(classroom)
edge1 = "EDGE1-AiO-Rv.2.txt"
edge1env = env.get_template(edge1)
edge2 = "EDGE2-AiO-Rv.2.txt"
edge2env = env.get_template(edge2)
edge3 = "EDGE3-AiO-Rv.2.txt"
edge3env = env.get_template(edge3)
edge4 = "EDGE4-AiO-Rv.2.txt"
edge4env = env.get_template(edge4)
distro1 = "DIST1-AiO-Rv.2.txt"
distro1env = env.get_template(distro1)
distro2 = "DIST2-AiO-Rv.2.txt"
distro2env = env.get_template(distro2)
distro5 = "DIST5-AiO-Rv.2.txt"
distro5env = env.get_template(distro5)
distro6 = "DIST6-AiO-Rv.2.txt"
distro6env = env.get_template(distro6)
distro7 = "DIST7-AiO-Rv.2.txt"
distro7env = env.get_template(distro7)
distro8 = "DIST8-AiO-Rv.2.txt"
distro8env = env.get_template(distro8)
distro9 = "DIST9-AiO-Rv.2.txt"
distro9env = env.get_template(distro9)
lanrtr7750old = "7750-48F_LANRTR_OldIPScheme.txt"
lanrtr7750oldenv = env.get_template(lanrtr7750old)
lanrtr7750new = "7750-48F_LANRTR_NewIPScheme.txt"
lanrtr7750newenv= env.get_template(lanrtr7750new)
lanrtr7850old = "7850-48FS_LANRTR_OldIPScheme.txt"
lanrtr7850oldenv = env.get_template(lanrtr7850old)
lanrtr7850new = "7850-48FS_LANRTR_NewIPScheme.txt"
lanrtr7850newenv = env.get_template(lanrtr7850new)
templanrtr = "L3TempRTR.txt"
templanrtrenv = env.get_template(templanrtr)


#Print section
print('')
print('')            
print("**********************************************")
print("**********************************************")
print("**********Starting Config Gen ***************")
print("**********************************************")
print("**********************************************")
print('')
print('')


#This generates the config files with the data depending on the model. Each model called out has to be typed correctly. Switch_data is pulled down from google sheets.
for i in switch_data:
    if 'Edge 1' in i.values():
        result = edge1env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'Edge 2' in i.values():
        result = edge2env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'Edge 3' in i.values():
        result = edge3env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'Edge 4' in i.values():
        result = edge4env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 1' in i.values():
        result = distro1env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 2' in i.values():
        result = distro2env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 5' in i.values():
        result = distro5env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 6' in i.values():
        result = distro6env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 7' in i.values():
        result = distro7env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 8' in i.values():
        result = distro8env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'DISTRO 9' in i.values():
        result = distro9env.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if 'Classroom' in i.values():
        result = classroomenv.render(i)
        f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
        f.write(result)
        f.close()
        print(str(i['NewSwitchHostname']) + ' Config Generated')

for i in switch_data:
    if new_old_vlan == "OLD":
        if 'LAN 7750' in i.values():
            result = lanrtr7750oldenv.render(i)
            f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
            f.write(result)
            f.close()
            tempconfig = templanrtrenv.render(i)
            s = open(os.path.join(home_folder, i['NewSwitchHostname'] + "TEMPRTR" + ".txt"), "w", encoding="utf-8")
            s.write(tempconfig)
            s.close()
            print(str(i['NewSwitchHostname']) + ' Config Generated + tempRTR')
    else:
        if 'LAN 7750' in i.values():
            result = lanrtr7750newenv.render(i)
            f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
            f.write(result)
            f.close()
            tempconfig = templanrtrenv.render(i)
            s = open(os.path.join(home_folder, i['NewSwitchHostname'] + "TEMPRTR" + ".txt"), "w", encoding="utf-8")
            s.write(tempconfig)
            s.close()
            print(str(i['NewSwitchHostname']) + ' Config Generated + tempRTR')


for i in switch_data:
    if new_old_vlan == "OLD":
        if 'LAN 7850' in i.values():
            result = lanrtr7850oldenv.render(i)
            f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
            f.write(result)
            f.close()
            tempconfig = templanrtrenv.render(i)
            s = open(os.path.join(home_folder, i['NewSwitchHostname'] + "TEMPRTR" + ".txt"), "w", encoding="utf-8")
            s.write(tempconfig)
            s.close()
            print(str(i['NewSwitchHostname']) + ' Config Generated + tempRTR')
    else:
        if 'LAN 7850' in i.values():
            result = lanrtr7850newenv.render(i)
            f = open(os.path.join(home_folder, i['NewSwitchHostname'] + ".txt"), "w", encoding="utf-8")
            f.write(result)
            f.close()
            tempconfig = templanrtrenv.render(i)
            s = open(os.path.join(home_folder, i['NewSwitchHostname'] + "TEMPRTR" + ".txt"), "w", encoding="utf-8")
            s.write(tempconfig)
            s.close()
            print(str(i['NewSwitchHostname']) + ' Config Generated + tempRTR')


#Print section
print('')
print('')            
print("**********************************************")
print("**********************************************")
print("**********Completed Config Gen ***************")
print("**********************************************")
print("**********************************************")
print('')
print('')




# This section below will upload the configuration files to the integrations drive/config dump.

# If modifying these scopes, delete the file token.pickle and recrete it.
SCOPES = ["https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]



# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

creds = None

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

#Print section
print("*************************************************")
print("*************************************************")
print("** Starting to upload the files to config dump **")
print("*************************************************")
print("*************************************************")
print('')
print('')


# This section creates a folder for the configs on the drive in config dump.
folder_metadata = {
    'name': site_code,
    'mimeType': 'application/vnd.google-apps.folder',
    'driveId' : 'XXXXXXXXXXXXXXXXXX',
    'parents' : ['XXXXXXXXXXXXXXXXX']
}

#executes the file creation
folder = service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()


#This section grabs the folder ID to update the parent.
folder_id = folder.get('id')

#This section returns a variable of the files in the site_folder.
configs = os.listdir(home_folder)

#This section loops through all files in the config and uploads them to the config dump
for files in configs:
    file_metadata = {'name': files,
                 'mimeType': '*/*',
                 'driveId' : 'XXXXXXXXXXXXXXXXXXXXXX',
                 'parents' : [folder_id]
    }
    media = MediaFileUpload(str(home_folder) + str(files),
                        mimetype='*/*',
                        resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id', supportsAllDrives=True).execute()
    print(str(files) + " Uploaded")


#Final print section.
print('')
print('')
print("ConfigGen script has completed.")
print('')
print('')




