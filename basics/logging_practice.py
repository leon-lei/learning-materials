# Code referenced from realpython.com/python-logging
import logging
import logging.config
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Set basic configurations such as format and level
# Uses default logger named root
logging.basicConfig(filename=os.path.join(BASE_DIR, 'logs', 'basicConfig.log'), format='%(asctime)s - %(levelname)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.warning('Admin logged out')


# Capture stack trace with exc_info parameter
# logging.exception should be called from exception handler
# Log level set at ERROR. If debug or critical is desired, use exc_info parameter
a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.debug("From logging.error with exc_info param:", exc_info=True)
    logging.exception("From logging.exception:")


# Define own logger from class
# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(os.path.join(BASE_DIR, 'logs', 'customLogger.log'))
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')


# Configure logger from yaml file 
with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

# Should not be written into errors.log
logging.debug('This is an debug message')
logging.info('This is an info message')
logging.warning('This is a warning')

# Should be written into errors.log
logging.error('This is a error message')
logging.critical('This is a critical message')