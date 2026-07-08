import requests
import json
import os
from datetime import datetime
import time
import logging

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

response = requests.get(url)
data = response.json()

#save our data locally
with open(filename,'w') as file:
    json.dump(data)

