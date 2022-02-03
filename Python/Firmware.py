#This section is for logging into the switches and generating the files
import subprocess, sys, netmiko, paramiko, threading
from netmiko import SCPConn
import socket
socket.setdefaulttimeout(5)
from concurrent import futures
from datetime import datetime
from getpass import getpass
import os, time

#This section is for google sheets auth and other modules needed
import gspread
import pandas as pd
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build


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
print('#######     Created by XXXXXXXXXXXXXXXXXXXXXXXXX    #######')
print('                                                           ')
print('                                                           ')
print('                            Firmware                       ')
print('                                                           ')
print('                                                           ')



#Global Variables
device_type = ('ruckus_fastiron')
username = input('TACACS Username? ')
password = getpass()
list_threads = []
link = 'googlesheetXXXXXXXXXXXXXXXXXX'

##Generates folder structure on the local machine to save the configuration files.
print()
site_code = input("What is the site code? This creates a folder for the files: ")
print()
school_folders = "C:\\Firmware\\Schools\\"
home_folder = school_folders + site_code + ("\\")
if not os.path.exists(school_folders + site_code ):
    os.mkdir(school_folders + site_code)


#Below authenticates you to the Google Drive/spreadsheets, the creds.json must be in the same file as script. See XXXXXXXXXXXXX to get a key.
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
get_gdrive_service = build('drive', 'v3', credentials=creds)
service = get_gdrive_service



#This will open up the specific google spreadsheet, and pull down the data from the configuration tab.
sheet = client.open_by_url(link)
worksheet = sheet.worksheet("ScriptLAN")
parameter = worksheet.get_all_records()
df = pd.DataFrame(parameter)
switch_data = df.to_dict('records')
switch_ip = df.iloc[:,3]



#Logs into the Sheet and appends a list of IP's to devices
devices = []
for i in switch_ip:
    devices.append(i)
device_count = len(devices)

#Commands for each switch

date = input("What is the date of the reboot? mm-dd-yy: ")
command1 = ('wr mem')
command2 = ('copy start tftp 10.x.x.x /ConfigsRTR/')
reboot_command = ('reload at 04:30:00 ' + date + ' pri')
command3 = ("copy tftp fl 10.x.x.x 08090k/ICX7750/Images/SWR08090kufi.bin pri")


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
            try:
                out_file.write(' ## Output of ' + command1 + '-' * 35 + '\n\n')
                out_file.write(connection.send_command(command1) + '\n\n')
            except:
                print ('\n[Command ERROR] -', command1, 'caused an error on', devices, '\n')
            try:
                out_file.write(' ## Output of ' + command2 + '-' * 35 + '\n\n')
                out_file.write(connection.send_command(command2 + devices) + '\n\n')
            except:
                print ('\n[Command ERROR] -', command2, 'caused an error on', devices, '\n')
            try:
                out_file.write(' ## Output of ' + reboot_command + '-' * 35 + '\n\n')
                out_file.write(connection.send_command(reboot_command) + '\n\n')
            except:
                print ('\n[Command ERROR] -', reboot_command, 'caused an error on', devices, '\n')
            try:
                out_file.write(' ## Output of ' + command3 + '-' * 35 + '\n\n')
                out_file.write(connection.send_command(command3) + '\n\n')
            except:
                print ('\n[Command ERROR] -', command3, 'caused an error on', devices, '\n')
                
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
        print()
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
    time.sleep(30)
    print(x)

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
print ('Elapsed time:', str(datetime.now() - starting_time))



