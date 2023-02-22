import logging
import csv

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Basic message levels format
"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""

try:
     with open('students.csv', 'w', newline='') as file:
         writer = csv.writer(file)
         
         writer.writerow(["No", "Name", "Subject"])
         writer.writerow([1, "Ash Ketchum", "English"])
         writer.writerow([2, "Gary Oak", "Mathematics"])
         writer.writerow([3, "Brock Lesner", "Physics"])


try:
    # some code that may raise an exception
    1/0
except Exception as e:
    logging.exception('An error occurred: {}'.format(str(e)))
