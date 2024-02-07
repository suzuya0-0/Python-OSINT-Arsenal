import subprocess

def get_wifi_profiles():
    """
    Retrieves the Wi-Fi profiles from the system.
    """
    try:
        wifi_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        return wifi_data
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []

def get_wifi_password(profile_name):
    """
    Retrieves the password for a given Wi-Fi profile.
    """
    try:
        show_pass = subprocess.check_output(["netsh", "wlan", "show", "profile", profile_name, "key=clear"]).decode("utf-8").split("\n")
        password = [line.split(":")[1][1:-1] for line in show_pass if "Key Content" in line]
        return password[0] if password else ""
    except (subprocess.CalledProcessError, IndexError) as e:
        print(f"Error: {e}")
        return ""

def main():
    """
    Main function to retrieve and display Wi-Fi profiles and passwords.
    """
    wifi_profiles = get_wifi_profiles()
    if not wifi_profiles:
        print("No Wi-Fi profiles found.")
        return
    
    usernames = [line.split(":")[1][1:-1] for line in wifi_profiles if "All User" in line]
    for username in usernames:
        password = get_wifi_password(username)
        print("{:<30}|  {:<}".format(username, password))

if __name__ == "__main__":
    main()
