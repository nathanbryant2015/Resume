import time
import yaml
import subprocess
import psutil

#Sleep for TV Screen to Power on
time.sleep(30) 


# Import yaml config file
# How to call variables: print(config['chrome_url02']) or x = config['chrome_url02']
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)


#Variables from config file
username = config["Nx_User"]
password = config["Nx_Pass"]
server_ip = config["Nx_Svr"]
nx_shortcut = config["Nx_Shortcut"]
nx_layout01_name = config["nx_layout01_name"]
nx_layout02_name = config["nx_layout02_name"]
screen_0_number = config["Nx_Screen_0"]
screen_1_number = config["Nx_Screen_1"]

# Loop every 4 hours
while True:
    #Selects the variables from the config file listed above
    cmd0 = f'"{nx_shortcut}" --auth=http://{username}:{password}@{server_ip}:7001 --no-fullscreen=false --layout-name "{nx_layout01_name}" --screen={screen_0_number}'
    cmd1 = f'"{nx_shortcut}" --auth=http://{username}:{password}@{server_ip}:7001 --no-fullscreen=false --layout-name "{nx_layout02_name}" --screen={screen_1_number}'

    #Executes the cmd variable/params
    process0 = subprocess.Popen(cmd0, shell=True)
    process1 = subprocess.Popen(cmd1, shell=True)

    # Define the name of the process to search for
    process_name = "HD Witness.exe"

    # Sleep for 4 hours (4 hours = 4 * 60 * 60 seconds)
    time.sleep(4 * 60 * 60)

    # Get a list of all running processes
    all_processes = psutil.process_iter()

    # Iterate over the processes and terminate HD Witness.exe
    for process in all_processes:
        if process.name() == process_name:
            process.terminate()

   