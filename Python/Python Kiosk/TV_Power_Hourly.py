import subprocess
import time

# Path to the PowerShell executable
powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'

# Path to the PowerShell script
script_path = r'C:\kiosk\Tv_Power_Hourly.ps1'


while True:
    # Command to execute the script
    command = [powershell_path, '-ExecutionPolicy', 'Unrestricted', '-File', script_path]

    # Launch the PowerShell script
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the process to finish and get the output
    stdout, stderr = process.communicate()

    # Decode the output
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    # Check the return code
    return_code = process.returncode
    if return_code == 0:
        time.sleep(1)
    else:
        print(f"Script execution failed with return code {return_code}.")
        print("Error Output:")
        print(stderr)
        time.sleep(1)
    time.sleep(60 * 60)