import yaml
import time
import multiprocessing
import subprocess
import time

time.sleep(10) #Sleep for 10 seconds to allow OS to boot up

def launch_script(script_path):
    subprocess.call(['python', script_path]) #Launch the script using the 'subprocess' module

if __name__ == '__main__':


    # Import yaml config file
    # How to call variables print(config['chrome_url02']) or x = config['chrome_url02']
    with open('c:\\kiosk\\config.yml') as z:
        config = yaml.safe_load(z)

    processes = []

    if config['TV_Power_Daily'] == True:
        print("TV_Power_Daily Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\TV_Power_Daily.py',))
        processes.append(process)
        process.start()

    if config['TV_Power_Hourly'] == True:
        print("TV_Power_Hourly Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\TV_Power_Hourly.py',))
        processes.append(process)
        process.start()

    # Loop through Kiosk Types to Execute second script
    if config['Dashboard_1_Screen'] == True:
        print("Dashboard_1_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Dashboard_1_Screen.py',))
        processes.append(process)
        process.start()

    if config['Dashboard_2_Screen'] == True:
        print("Dashboard_2_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Dashboard_2_Screen.py',))
        processes.append(process)
        process.start()

    if config['NxWitness_1_Screen'] == True:
        print("NxWitness_1_Screens Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\NxWitness_1_Screen.py',))
        processes.append(process)
        process.start()

    if config['NxWitness_2_Screen'] == True:
        print("NxWitness_2_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\NxWitness_2_Screen.py',))
        processes.append(process)
        process.start()

    if config['NxWitness_3_Screen'] == True:
        print("NxWitness_3_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\NxWitness_3_Screen.py',))
        processes.append(process)
        process.start()

    if config['NxWitness_4_Screen'] == True:
        print("NxWitness_4_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\NxWitness_4_Screen.py',))
        processes.append(process)
        process.start()

    if config['Image_1_Screen'] == True:
        print("Image_1_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Image_1_Screen.py',))
        processes.append(process)
        process.start()

    if config['Image_2_Screen'] == True:
        print("Image_2_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Image_2_Screen.py',))
        processes.append(process)
        process.start()

    if config['Video_Loop'] == True:
        print("Video_Loop Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Video_Loop.py',))
        processes.append(process)
        process.start()

    if config['Screen_Saver_1_Screen'] == True:
        print("Screen_Saver_1_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Screen_Saver_1_Screen.py',))
        processes.append(process)
        process.start()

    if config['Screen_Saver_2_Screen'] == True:
        print("Screen_Saver_2_Screen Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Screen_Saver_2_Screen.py',))
        processes.append(process)
        process.start()

    if config['Mac_Update'] == True:
        print("Mac_Update Script Executed")
        process = multiprocessing.Process(target=launch_script, args=(r'C:\kiosk\Mac_Update.py',))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Startup Script Complete")
