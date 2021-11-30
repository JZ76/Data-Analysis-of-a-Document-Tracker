#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" main """

__author__ = "Jiancheng Zhang and Haoran Hong"

import sys
import getopt
import os
import re
from Task2 import t2

from Task4 import t4

def help():
    print("###########################################################################################\n")
    print("options:")
    print("\t-u  --userID: input the userID that need to query (Optional)")
    print("\t-d  --docID: input the documentID that need to query")
    print("\t-t  --taskID: input one of the task that want to run, [2a, 2b, 3a, 3b, 4, 5d, 6, 7]")
    print("\t-f  --filename: input the JSON file that contains the data")
    print("\t-h  --help: ask for help")
    print("\t-q  --quit: exit immediately\n")
    print("###########################################################################################")


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:d:t:f:hq',
                                   ['userID=', 'docID=', 'taskID=', 'filename=', 'help', 'quit'])
        fileName = ""
        userID = 0
        docID = 0
        task_id = 0
        for opt_name, opt_value in opts:
            if opt_name in ('-u', '--userID'):
                userID = opt_value
            elif opt_name in ('-d', '--docID'):
                docID = opt_value
            elif opt_name in ('-t', '--taskID'):
                if opt_value in ('2a', '2b', '3a', '3b', '4', '5d', '6', '7'):
                    task_id = opt_value
                else:
                    print("Unknown task ID", opt_value)
                    exit()
            elif opt_name in ('-f', '--filename'):
                file_exists = os.path.isfile(opt_value)
                if file_exists:
                    pattern = re.compile(r'\.json\Z')
                    t = pattern.search(opt_value)
                    if t is not None:
                        fileName = os.path.abspath(opt_value)
                    else:
                        print("Wrong file type:", opt_value, "not a json file.")
                        exit()
                else:
                    print("Cannot find file", opt_value, "because it does not exist.")
                    exit()
            elif opt_name in ('-h', '--help'):
                help()
                exit()
            elif opt_name in ('-q', '--quit'):
                exit()

        if fileName == "":
            print("No file input!")
            exit()
        if task_id == 0:
            print("No given task ID!")
            exit()
        if task_id == "2a":
            t2.view_by_country(docID, fileName)
        elif task_id == "2b":
            t2.view_by_continent(docID, fileName)
        elif task_id == "3a":
            print(task_id)
        elif task_id == "3b":
            print(task_id)
        elif task_id == "4":
            t4.top_10_reader(fileName)

        elif task_id == "5d":
            print(task_id)
        elif task_id == "6":
            print(task_id)
        elif task_id == "7":
            print(task_id)

    except getopt.GetoptError as error:
        print(error, "\n")
        help()
        sys.exit(2)
