import logging
from datetime import datetime
import os
import time

#so the function doesn't get upset
logger = logging.getLogger(__name__)

def setup_logger(timestamp:str,log_dir:str):
    """
    This initializes the logger for everything
    
    Args:
        timestamp(str): For the filename of the log.
        log_dir(str): Where the logs should be stored.
    """

    os.makedirs(log_dir, exist_ok =True)
    log_filename = f'{log_dir}/{timestamp}.log'

    logging.basicConfig(
        filename=log_filename,
        format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )

    return logging.getLogger()