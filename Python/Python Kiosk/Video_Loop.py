import subprocess
import time
import yaml

#Sleep for TV Screen to Power on
time.sleep(30) 

# Import yaml config file
# How to call variables: print(config['chrome_url02']) or x = config['chrome_url02']
with open('c:\\kiosk\\config.yml') as z:
    config = yaml.safe_load(z)

# Specify the path to the video and media player
vlc_path = config['video_player_path']
video_path = config['Video_location']


while True:
    # Launch VLC media player
    subprocess.Popen([vlc_path, "-f", "-L", "--no-osd", "--mouse-hide-timeout=1", "--no-video-title-show", "--video-on-top", video_path])

    # Delay for 2 hours
    time.sleep(2 * 60 * 60)
    

    # Kill VLC process
    subprocess.call(["taskkill", "/F", "/IM", "vlc.exe"])
