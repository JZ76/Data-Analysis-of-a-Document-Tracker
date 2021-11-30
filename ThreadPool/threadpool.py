#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" threadpool """


import threading
from concurrent.futures import ThreadPoolExecutor


def threadpool_execute(docID, dataset, func, result):
    remain = len(dataset) % 8
    lock = threading.RLock()
    args = ((lock, docID, dataset[i:i + len(dataset) // 8], result)
            for i in range(0, len(dataset), len(dataset) // 8))
    with ThreadPoolExecutor() as executor:
        if remain == 0:
            executor.map(lambda f: func(*f), args)
        else:
            executor.submit(func, (lock, docID, dataset, result))
