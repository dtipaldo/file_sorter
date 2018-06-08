import os
import json
import argparse
import logging


"""
sorter by Dan Tipaldo 06-2018


"""


# sort_file Method
def sort_file():
    pass
# Creates directory if required


if __name__ == '__main__':

    # Config File Definition
    config_file = 'sorter_configuration.json'

    # Sort Log Definition
    sort_log = 'sort_log'

    # Import and check User arguments (file or directory)

    # import and check logs and config file
    if sort_log:
        logging.basicConfig(filename=sort_log, level=logging.DEBUG)
    else:
        logging.warning('No log file set! All status will be displayed in the terminal only.')

    # if all information provided sort file


    pass

