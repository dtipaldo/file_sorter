import os
import datetime
import json
import argparse
import logging


"""
sorter by Dan Tipaldo 06-2018

"""
class File_Sorter(object):
    def __init__(self, config_file=None, sort_log=None):
        self.config_file = config_file
        self.sort_log = sort_log

        if sort_log:  # Log to file if defined, otherwise only log to screen
            logging.basicConfig(filename=sort_log, level=logging.INFO)
        else:
            logging.warning('No log file set! Sorter status will be displayed in the terminal only.')

        logging.info('Sorter Initialized at {}'.format(datetime.datetime.now()))


    def get_all_filepaths(path: str):
        """
        Method to identify all files recursively within a directory. Returns a list of full file paths

        :param path: directory path
        :type path: String
        :return: List of all files contained (recursively) within the directory path. Each item is a full path to the file
        :rtype: List
        """
        all_filepaths = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            all_filepaths.extend(list(map(lambda f: os.path.join(dirpath, f), filenames)))

        return all_filepaths


    # sort Method
    def sort(filepath: str):
        sort_result = False
        source_path = filepath


        destination_path =

        # Move file from source to destination

        return sort_result


if __name__ == '__main__':

    config_file = 'sorter_configuration.json'  # Config File Definition

    sort_log = 'sort_log'  # Sort Log Definition

    parser = argparse.ArgumentParser()  # Import and check User arguments (file or directory)
    parser.add_argument("path", help="String: filepath of the file(s) to sort. This can be a directory "
                                     "path or a file path")
    args = parser.parse_args()
    path = args.path

    file_sorter = File_Sorter(config_file, sort_log)

    if os.path.isfile(path):  # Send files straight to sorter
        file_sorter.sort(path)
    elif os.path.isdir(path):  # Make List of files from a directory to send to the sorter individually
        all_filepaths = file_sorter.get_all_filepaths(path)
        for path in all_filepaths:
            file_sorter.sort(path)
    else:
        logging.warning('{} is not a directory or file path'.format(path))


