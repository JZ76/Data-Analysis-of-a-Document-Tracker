#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" plot """

from functools import wraps
from matplotlib import pyplot as plt
import time
import threading
import itertools, sys

def plot_histogram(func):
    @wraps(func)
    def wrap_function(*args, **kwargs):
        results = None
        def spinner():
            spinner = itertools.cycle(['-', '\\', '|', '/'])
            while results is None:
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                sys.stdout.write('\b')
                time.sleep(0.1)
        print("Start analyzing data...", end="")
        spinning = threading.Thread(target=spinner)

        spinning.start()
        start_time = time.time()
        results = func(*args, **kwargs)
        spinning.join()
        if len(results) == 0:
            print("Nothing found in the file", args[-1])
        plt.figure(figsize=(12, 10), dpi=300)
        plt.bar(list(x[0:20] for x in list(results.keys())), list(results.values()), 0.6, align='center')
        plt.title(func.__name__)
        print("\nAnalyzing data duration(s):", time.time() - start_time)

        start_time = time.time()
        plt.show()
        print("Plotting data duration(s):", time.time() - start_time)

    return wrap_function


