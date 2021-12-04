#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" We will cut each chunk into 8 parts, each part is a task for a thread.
    if some chunk cannot divided by 8, means the size must less than 100000, we can directly submit to pool."""


import threading
from concurrent.futures import ThreadPoolExecutor


def threadpool_execute(userID, docID, dataset, func, result):
    """
    Due to if the thread has to write into the result dictionary, it has to get the lock first. So, the number of worker
    cannot be too many, otherwise the competition will slow down the speed.
    :param userID: some task will use this
    :param docID: some task will use this
    :param dataset: the size is (0,100000]
    :param func: each task has their own method to handle data
    :param result: is a dictionary, shared by all thread
    """
    remain = len(dataset) % 8
    # when initialize the thread pool, creat a lock. the thread has to get this lock first and then can write the result
    lock = threading.RLock()
    with ThreadPoolExecutor() as executor:
        if remain == 0:
            # creat args iterator
            args = ((lock, userID, docID, dataset[i:i + len(dataset) // 8], result)
                    for i in range(0, len(dataset), len(dataset) // 8))
            executor.map(lambda f: func(*f), args)
        else:
            executor.submit(lambda f: func(*f), [lock, userID, docID, dataset, result])
