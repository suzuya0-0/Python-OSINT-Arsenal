import os
import time

def get_wifi_profiles():
    os.system("netsh wlan show profile > ssids")
    with open('ssids', 'r') as file1:
        lines = file1.readlines()
        ssids = [line.strip().replace("All User Profile     : ", "") for line in lines if "All User Profile" in line]
    return ssids

def get_passwords(ssids):
    passwords = []
    for ssid in ssids:
        os.system(f'netsh wlan show profile "{ssid}" key=clear > ssid_data')
        time.sleep(0.3)
        with open('ssid_data', 'r') as file2:
            lines = file2.readlines()
            for line in lines:
                if "Key Content" in line:
                    line_data = line.strip().replace("Key Content            : ", "")
                    passwords.append("None" if line_data == " " else line_data)
                elif "Open" in line:
                    passwords.append("None")
    return passwords

def print_wifi_info(ssids, passwords):
    for ssid, password in zip(ssids, passwords):
        print(f"SSID: {ssid} PASSWORD: {password}")

def main():
    ssids = get_wifi_profiles()
    passwords = get_passwords(ssids)
    print_wifi_info(ssids, passwords)


    time.sleep(0.5)

    os.system("del ssid_data")
    os.system("del ssids")

    return ssids, passwords


if __name__ == "__main__":
    main()
