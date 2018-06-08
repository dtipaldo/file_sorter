import os
import datetime
import json
import argparse
import logging


"""
sorter by Dan Tipaldo 06-2018


"""


# sort_file Method
def sort_file(filepath: str):
    pass
# Creates directory if required


if __name__ == '__main__':

    config_file = 'sorter_configuration.json' # Config File Definition

    sort_log = 'sort_log' # Sort Log Definition

    parser = argparse.ArgumentParser() # Import and check User arguments (file or directory)
    parser.add_argument("path", help="String: filepath of the file(s) to sort. This can be a directory path or a file path")
    args = parser.parse_args()
    path = args.path

    if sort_log:  # Log to file if defined, otherwise only log to screen
        logging.basicConfig(filename=sort_log, level=logging.INFO)
    else:
        logging.warning('No log file set! Sorter status will be displayed in the terminal only.')
    logging.info('Sorter Initialized at {}'.format(datetime.datetime.now()))

    if os.path.isfile(path): # Send files straight to sorter
        pass
    elif os.path.isdir(path): # Make List of files in a directory to send to the sorter individually
        pass
    else:
        logging.warning('{} is not a directory or file path'.format(path))


