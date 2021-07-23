import requests
from bs4 import BeautifulSoup
import time

userlist = ["lustylanka"] # <--- INPUT USERNAMES HERE!!!
interval = 5 # <--- NUMBER OF MINUTES BETWEEN SAMPLES!!!


base = "https://xhamster.com/users/"
num_users = len(userlist)
user_log = [0]*num_users
count = 1;

while(True):
    for i in range(num_users):
        name = userlist[i]
        page = requests.get(base+name)
        soup = BeautifulSoup(page.content, "html.parser")
        offline = len(soup.find_all("div", class_="offline"))
        user_log[i] = user_log[i] + ((offline==0)*interval)
        print(name + ":\tOnline for " + str(user_log[i]) + "min out of " + str(count*interval) + "min")
        
    print("")
    count = count + 1
    time.sleep(60*count*interval)
