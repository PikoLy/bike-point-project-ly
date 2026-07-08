import requests
import json
import os
from datetime import datetime
import time
import logging

# set up our variables

url = 'https://api.tfl.gov.uk/BikePoint/'
#creating a data directory and error handling, naming the folder data
data_dir = 'data'
#creating the directory/folder
os.makedirs('data', exist_ok=True)
# creating timestamp for filename and format datetime as a string
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10


# step two, starting our while loop
while attempt < max_retry:
    response = requests.get(url)
    #for status look at hte error code
    status = response.status_code
    if 200 <=status < 300:
        data = response.json()
        #save our data locally
        with open(filename,'w') as file:
            json.dump(data,file)
        print('yay🥳')
        #stop the loop
        break
    elif status <=100 or status >=500:
        #retry but after delay
        time.sleep(delay)
        print('retrying')
        attempt+=1
    else:
        print('fix something')
        print(status)
        break




