#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" threadpool """

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat


def threadpool_execute(docID, dataset, func, result):
    with ThreadPoolExecutor() as executor:
        remain = len(dataset) % 8
        if remain == 0:
            executor.map(func,
                         repeat(docID),
                         [dataset[i:i + len(dataset) // 8] for i in range(0, len(dataset) - len(dataset) // 8, len(dataset) // 8)],
                         repeat(result))
        else:
            executor.submit(func, [docID, dataset, result])
