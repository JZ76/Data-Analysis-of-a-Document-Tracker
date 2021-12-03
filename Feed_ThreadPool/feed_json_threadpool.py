#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" * """

from FileIO import fileIO as fio
from ThreadPool import threadpool as tp
import os
import re

def feed_json_into_Threadpool(userID, docID, filename, process_method):
    file_exists = os.path.isfile(filename)
    if file_exists:
        pattern = re.compile(r'\.json\Z')
        t = pattern.search(filename)
        if t is not None:
            filename = os.path.abspath(filename)
            result = {}
            for chunk in fio.chunks(filename):
                tp.threadpool_execute(userID, docID, chunk, process_method, result)
            return result
        else:
            print("Wrong file type:", filename, "not a json file.")
            exit()
    else:
        print("Cannot find file", filename, "because it does not exist.")
        exit()
