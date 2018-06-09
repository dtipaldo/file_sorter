import os
import datetime
import json
import argparse
import logging
import re


"""
sorter by Dan Tipaldo 06-2018

"""
class File_Sorter(object):
    def __init__(self, config_file=None, sort_log=None):
        self.sort_log = sort_log
        if self.sort_log:  # Log to file if defined, otherwise only log to screen
            logging.basicConfig(filename=self.sort_log, level=logging.INFO)
        else:
            logging.warning('No log file set! Sorter status will be displayed in the terminal only.')

        logging.info('{} - Sorter Initialized'.format(datetime.datetime.now()))

        try:
            self.patterns = json.loads(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), config_file), "r").read())
        except FileNotFoundError:
            logging.warning("Config File not found")  # TODO: Add more exceptions

    def get_all_filepaths(self, path: str):
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

    def sort(self, filepath: str):
        filename = os.path.basename(filepath)
        for destination in self.patterns.keys():
            for pattern in self.patterns[destination]['patterns']:
                p = re.compile(pattern)
                if p.match(filename):
                    try:
                        os.rename(filepath, os.path.join(destination, filename))
                        logging.info('{} - Sorting File {} ==> {}'.format(datetime.datetime.now(), filepath, os.path.join(destination, filename)))
                        print('{} - Sorting File {} ==> {}'.format(datetime.datetime.now(), filepath, os.path.join(destination, filename)))
                    except FileExistsError:
                        logging.warning("{} already exists".format(os.path.join(destination, filename)))
        return


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


