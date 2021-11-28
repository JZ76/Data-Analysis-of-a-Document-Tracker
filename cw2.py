#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" main """

__author__ = "Jiancheng Zhang and Haoran Hong"

import sys
import getopt
import os


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
        args_list = [0] * 2
        task_id = 0
        for opt_name, opt_value in opts:
            if opt_name in ('-u', '--userID'):
                args_list[0] = opt_value
            elif opt_name in ('-d', '--docID'):
                args_list[1] = opt_value
            elif opt_name in ('-t', '--task'):
                if opt_value in ('2a', '2b', '3a', '3b', '4', '5d', '6', '7'):
                    task_id = opt_value
                else:
                    print("Unknown task ID", opt_value)
                    exit()
            elif opt_name in ('-f', '--filename'):
                file_exists = os.path.isfile(opt_value)
                if file_exists:
                    fileName = opt_value
                    print(opt_value)
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
            print(task_id)
        elif task_id == "2b":
            print(task_id)
        elif task_id == "3a":
            print(task_id)
        elif task_id == "3b":
            print(task_id)
        elif task_id == "4":
            print(task_id)
        elif task_id == "5d":
            print(task_id)
        elif task_id == "6":
            print(task_id)
        elif task_id == "7":
            print(task_id)

    except getopt.GetoptError as error:
        print(error, "\n")
        help()
