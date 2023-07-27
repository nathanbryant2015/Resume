import psutil
import gspread
import socket
from oauth2client.service_account import ServiceAccountCredentials

# Define your Google Spreadsheet credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive",
         "https://www.googleapis.com/auth/drive.appdata"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Kiosk\\backend\\macupdatecreds.json', scope)
client = gspread.authorize(credentials)

# Specify the name of the Google Spreadsheet and the worksheet
main_page = 'https://LINK-Goes-HERE'
sheet = client.open_by_url(main_page)
worksheet = sheet.worksheet("Master")

# Get the list of network interfaces and their statistics
nic_stats = psutil.net_io_counters(pernic=True)

# Sort the network interfaces by the number of bytes sent and received
sorted_nics = sorted(nic_stats.items(), key=lambda x: x[1].bytes_sent + x[1].bytes_recv, reverse=True)

# Find the active NIC (interface with the highest number of bytes sent/received)
active_nic = None
for nic, _ in sorted_nics:
    if nic.startswith('Ethernet') or nic.startswith('Wi-Fi'):
        active_nic = nic
        break

if active_nic is None:
    print("No active NIC found.")
else:
    # Get the host name
    host_name = socket.gethostname()

    # Get the MAC address
    mac_address = ''.join(filter(lambda x: x.isalnum(), psutil.net_if_addrs()[active_nic][0].address))
    mac_address = ':'.join(mac_address[i:i+2] for i in range(0, len(mac_address), 2))
    print(mac_address)

    # Get the IP address
    ip_address = None
    for addr in psutil.net_if_addrs()[active_nic]:
        if addr.family == socket.AF_INET:
            ip_address = addr.address
            break

    print(ip_address)

    # Find the cell containing the MAC address and update the adjacent cells with the host name and IP address
    try:
        cell = worksheet.find(mac_address)
        worksheet.update_cell(cell.row, cell.col - 1, host_name)
        worksheet.update_cell(cell.row, cell.col + 1, ip_address)
        print("Cell updated successfully!")
    except gspread.exceptions.CellNotFound:
        print("MAC address not found in the worksheet.")

print("Mac_Update Script Finished")



