import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


try:
    # some code that may raise an exception
    1/0
except Exception as e:
    logging.exception('An error occurred: {}'.format(str(e)))
