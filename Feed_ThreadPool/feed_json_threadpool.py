#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" We feed each chunk from json file into thread pool, and check for file path again, because there is no file path
    check after user input that from GUI."""
import sys

from FileIO import fileIO as fio
from ThreadPool import threadpool as tp
import os
import re

def feed_json_into_Threadpool(userID, docID, filename, process_method):
    """
    Each task has different process method, but not all of them need userID or docID, but better to include them
    to provide future functions extension.

    Parameters:
        param1 - this is the first param
        param2 - this is a second param

    Returns:
        This is a description of what is returned

    Raises:
        KeyError - raises an exception
    """
    file_exists = os.path.isfile(filename)
    if file_exists:
        pattern = re.compile(r'\.json\Z')
        t = pattern.search(filename)
        if t is not None:
            filename = os.path.abspath(filename)
            result = {}
            # use “lazy data structures” here, only read next chunk when next iteration
            for chunk in fio.chunks(filename):
                tp.threadpool_execute(userID, docID, chunk, process_method, result)
            return result
        else:
            print("Wrong file type:", filename, "not a json file.")
            sys.exit(1)
    else:
        print("Cannot find file", filename, "because it does not exist.")
        sys.exit(1)
