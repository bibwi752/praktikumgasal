# import subprocess
# from pyfiglet import figlet
# import colorama

# colorama.init()
# f = figlet(font='big')
# print(colorama.fore.GREEN + f.rendertext('tiyanmoe'))

# profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

# profile_name = [i.split(':')[1][1:-1] for i in profiles if "ALL user profile"in i]

# print("{:<}| {:,}".format("Wi-Fi Name", "password"))
# print("---------------------------------------------")

# for name in profile_names:
#     try:
#         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
#         password = [line.split(':')[1][1:-1] for line in rwsults if 'Key Content' in line][0]
#         #password = [Line.spLIt(":")[1][1:-1] for Line in results if 'key content' in Line]


#         print("{:<30}| {:<}".format(name,npassword))

#         except:
#             print("{:<30}| {:<}".format(na,e, "Not foud"))


# import subprocess
# from pyfiglet import Figlet
# import colorama

# colorama.init()
# f = Figlet(font='big')
# print(colorama.Fore.GREEN + f.renderText('tiyanmoe'))

# profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

# profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
# print("-----------------------------------------------")

# for name in profile_names:
#     try:
#         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
#         password = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line][0]
#         # password = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]

        
#         print("{:<30}| {:<}".format(name, password))
    
#     except:
#         print("{:<30}| {:<}".format(name, "Not Found"))




# import subprocess
# from pyfiglet import Figlet
# import colorama

# colorama.init()
# f = Figlet(font='big')
# print(colorama.Fore.GREEN + f.renderText('tiyanmoe'))

# profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

# profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
# print("-----------------------------------------------")

# for name in profile_names:
#     try:
#         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
#         password = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line][0]
#         # password = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]

        
#         print("{:<30}| {:<}".format(name, password))
    
#     except:
#         print("{:<30}| {:<}".format(name, "Not Found"))


# import subprocess
# from pyfiglet import Figlet
# import colorama

# colorama.init()
# f = Figlet(font='big')
# print(colorama.Fore.GREEN + f.renderText('tiyanmoe'))

# profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

# profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
# print("-----------------------------------------------")

# for name in profile_names:
#     try:
#         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
#         password = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line][0]
#         # password = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]

        
#         print("{:<30}| {:<}".format(name, password))
    
#     except:
#         print("{:<30}| {:<}".format(name, "Not Found"))


import subprocess
from pyfiglet import Figlet
import colorama

colorama.init()
f = Figlet(font='big')
print(colorama.Fore.GREEN + f.renderText('tiyanmoe'))

profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')[1:]

profile_names = [i.split(':')[1][1:-1] for i in profiles if "All User Profile" in i]

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-----------------------------------------------")

for name in profile_names:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
        password = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line][0]
        # password = [line.split(":")[1][1:-1] for line in results if 'Key Content' in line]

        
        print("{:<30}| {:<}".format(name, password))
    
    except:
        print("{:<30}| {:<}".format(name, "Not Found"))














