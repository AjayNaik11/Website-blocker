# import time
# from datetime import datetime as dt 
# import os
# import platform

# # Detect OS and set the correct hosts file path
# if platform.system() == "Windows":
#     host_path = r"C:\Windows\System32\drivers\etc\hosts"
# else:
#     host_path = "/etc/hosts"  # Linux/macOS path


# ip_local_machine = "127.0.0.1"
# blocked_website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.instagram.com", "instagram.com"]
# work_start_time = "09:00:00"
# work_end_time = "23:00:00"


# now = dt.now()

# while True:
#     current_time = now.strftime("%H:%M:%S")
#     if current_time >= work_start_time and current_time <= work_end_time:
#         print("Working hours...")
#         with open(host_path, 'r+') as file:
#             content = file.read()
#             for website in blocked_website_list:
#                 if website in content:
#                     pass
#                 else:
#                     file.write(ip_local_machine + " " + website + "\n")
#     else:
#         print("non working hours.....")
#         with open(host_path, 'r+') as file:
#             content = file.readlines()
#             file.seek(0)
#             for line in content:
#                 if not any(website in line for website in blocked_website_list):
#                     file.write(line)
#             file.truncate()
#     time.sleep(10)


import time
from datetime import datetime as dt
import os
import platform

# Detect OS and set the correct hosts file path
if platform.system() == "Windows":
    host_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    host_path = "/etc/hosts"  # Linux/macOS path

ip_local_machine = "127.0.0.1"
blocked_website_list = [
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.instagram.com", "instagram.com"
]

work_start_time = "09:00:00"
work_end_time = "23:00:00"

while True:
    # Update current time inside loop
    current_time = dt.now().strftime("%H:%M:%S")

    if work_start_time <= current_time <= work_end_time:
        print("Working hours... Blocking websites")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in blocked_website_list:
                if website not in content:
                    file.write(ip_local_machine + " " + website + "\n")
    else:
        print("Non-working hours... Unblocking websites")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_website_list):
                    file.write(line)
            file.truncate()

    # Sleep for 10 seconds before checking again
    time.sleep(10)
