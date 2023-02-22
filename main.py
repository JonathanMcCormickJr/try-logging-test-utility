import logging
import csv

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    with open("students.csv", 'r') as file:
        csvreader = csv.reader(file)
            
        for row in csvreader:
            # do something
            somehitn = 4
except FileNotFoundError:
    logging.error("ERROR: students.csv could not be found or is empty.")