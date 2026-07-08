import requests
import json
import os
from datetime import datetime
import time
import logging

#set up logging
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir ='logs'
os.makedirs(log_dir, exist_ok =True)
log_filename = f'{log_dir}/{timestamp}'

logging.basicConfig(
    filename=log_filename,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger()
logger.info('Logger successfully initialized')

# set up our variables
url = 'https://api.tfl.gov.uk/BikePoint/'
#creating a data directory and error handling, naming the folder data
data_dir = 'data'
#creating the directory/folder
os.makedirs('data', exist_ok=True)
# creating timestamp for filename and format datetime as a string

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
        # checking if we are saving data in our json file by checking hte size or len
        if len(data) > 1:
            try:
                #save our data locally
                with open(filename,'w') as file:
                    json.dump(data,file)
                print('yay🥳')
                logger.info(f'File {filename} was successfully saved')
            except Expection as e:
                logger.error(f'An error occured: {e}')
                #stop the loop
            break
        else:
            logger.error('No data returned')
            break
    elif status <=100 or status >=500:
        #retry but after delay
        time.sleep(delay)
        print('retrying')
        logger.info(f'Status code {status}. Retrying. This was attempt {attempt}')
        attempt+=1
       
    else:
        print('fix something')
        print(status)
        logger.error(f'Error. Status code {status}. Fix it')
        break




