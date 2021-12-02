#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" threadpool """


import threading
from concurrent.futures import ThreadPoolExecutor


def threadpool_execute(userID, docID, dataset, func, result):
    remain = len(dataset) % 8
    lock = threading.RLock()
    with ThreadPoolExecutor() as executor:
        if remain == 0:
            args = ((lock, userID, docID, dataset[i:i + len(dataset) // 8], result)
                    for i in range(0, len(dataset), len(dataset) // 8))
            executor.map(lambda f: func(*f), args)
        else:
            executor.submit(lambda f: func(*f), [lock, userID, docID, dataset, result])
