#This section is for logging into the switches and generating the validation files
import subprocess, sys, netmiko, paramiko, threading
import socket
socket.setdefaulttimeout(5)
from concurrent import futures
from datetime import datetime
from getpass import getpass
import os, time

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
print('                    SSH Script                             ')
print('                                                           ')
print('                                                           ')


#Variables for netmiko, Use's text file rather than googles API
devices = open('./devices.txt', 'r').read().split('\n')
device_type = ('ruckus_fastiron')
username = input('TACACS Username? ')
password = getpass()
errDevice = []
err = 0
device_count = len(devices)
list_threads = []

##Generates folder structure on the local machine to save the configuration files.
site_code = input("What is the site code? This creates a folder for the files: ")
print('')
print('')
school_folders = "C:\\Scripts\\Validation\\Schools\\"
home_folder = school_folders + site_code + ("\\")
if not os.path.exists(school_folders + site_code ):
    os.mkdir(school_folders + site_code)


#This section is for the google drive folder that the files will be uploaded to
folder_id = input("What is the Google Drive Validation folder ID? ")


#commands to run for each switch.
commands = ('show cli-command-history', 'wr mem', 'show stack', 'show license', 'show version', 'show flash', 'show boot', 'show aaa', 'show media validation', 'show interface brief wide',
            'show lldp neighbor', 'show statistics',' show run')

starting_time = datetime.now()

#Connection to the devices and the commands will be executed.
def conn(devices):
    global errDevice
    global err
    global username,password

    try:
        connection = netmiko.ConnectHandler(ip=devices,
                                            device_type=device_type,
                                            username=username,
                                            password=password,
                                            global_delay_factor=1)
        filename = connection.base_prompt + '_' + devices + '.txt'
        with open(os.path.join(home_folder + filename),'w') as out_file:
            for command in commands:
                try:
                    out_file.write(' ## Output of ' + command + '-' * 35 + '\n\n')
                    out_file.write(connection.send_command(command) + '\n\n')
                except:
                    print ('\n[Command ERROR] -', command, 'caused an error on', devices, '\n')
                    errDevice.append(errDevices)
                    err += 1
        print('\n[INFO] - ', filename, 'has finished.\n')
        connection.disconnect()
    except netmiko.ssh_exception.NetMikoTimeoutException:
        print('\n********[ERROR] SSH Issue ' + devices)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print('\n********[ERROR] - Authentication error to:', devices, '\n')
    except ValueError:
        print()
    except socket.timeout:
        print('\n********[ERROR] SSH Issue', devices, '\n')
    except UnboundLocalError:
        print('\n********[ERROR] UnboundLocalError:', devices, '\n')
    except paramiko.ssh_exception.SSHException:
         print('\n********[ERROR] SSH Issue P', devices, '\n')
    except paramiko.ssh_exception.AuthenticationException:
        print('\n********[ERROR] - Authentication error to:', devices, '\n')
    except ValueError:
        print('\n********[ERROR] - ValueError error to:', devices, '\n')
    except OSError:
        print('\n********[ERROR] - Not a Ruckus Device:', devices, '\n')
    except Exception:
        print('\n********[ERROR] - Input was not an IP address:', devices, '\n')
        
#This section starts the Threading process and starts threads for the amount of devices
try:
    count=0
    print("")
    print("Generating Pool and Logging into devices, This may take a while depending on the amount of devices. ")
    print("")
    while count<len(devices):
        for i in range(175):
            x = threading.Thread(target=conn,args=(str(devices[count]),))
            count+=1
            list_threads.append(x)
except Exception as e:
    print("")

#Starts the thread pool.
for x in list_threads:
    x.start()
    time.sleep(1.0)

#ends the thread pool and after this loop the code will continue.
for x in list_threads:
    x.join()
    

#Print section
print('')
print('')            
print("**********************************************")
print("**********************************************")
print("********** File Generation Complete **********")
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
        creds = flow.run_local_server(port=80)
# Save the credentials for the next run.
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

#Call to google API drive.
service = build('drive', 'v3', credentials=creds)

#Print section
print("*************************************************")
print("*************************************************")
print("Starting to upload the files to Validation folder")
print("*************************************************")
print("*************************************************")
print('                                                           ')
print('                                                           ')


#This section returns a variable of the files in the site_folder.
configs = os.listdir(home_folder)

#This section loops through all files in the config and uploads them to the Validaiton folder created.
for files in configs:
    file_metadata = {'name': files,
                 'mimeType': '*/*',
                 'driveId' : 'XXXXXXXXXXXXXXXXX',
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
print("Validaiton script has completed. Check Validation folder for files.")
print('')
print('')
print ('Elapsed time:', str(datetime.now() - starting_time))


