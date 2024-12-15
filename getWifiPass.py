import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')

profiles=[profile.split(":")[1][1:-1] for profile in data if "All User Profile" in profile]

print("{:<20}| {:}\n".format('Wi-Fi Names', 'Password'))

for profile in profiles:
     data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
     data = data.decode('uft-8').split('\n')
     
     password = [passw.split(":")[1][1:-1] for passw in data if "Key Content" in passw]
     
     try:
         print("{:<20}| {:}".format(profile, password[0]))
     except IndexError:
        print("{:<20}| {:}".format(profile, ""))