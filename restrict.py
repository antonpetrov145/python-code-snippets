import time 
from datetime import datetime as dt 


website_list = ["https://www.youtube.com","youtube.com","www.youtube.com", "https://www.facebook.com", "facebook.com", "www.facebook.com"]
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        f = open(r"C:\Windows\System32\drivers\etc\hosts", "r+")
        contents = f.read()
        for site in website_list:
                if site in contents:
                    pass
                else:
                    f.write(redirect + " " + site + "\n")
    else:
        f = open(r"C:\Windows\System32\drivers\etc\hosts", "r+")
        contents = f.read()
        f.seek(0)
        for line in contents:
            if not any(site in line for site in website_list):
                f.write(line)
            f.truncate()
            print("Fun Hours ...")