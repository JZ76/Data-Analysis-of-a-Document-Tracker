#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" plot_histogram is a decorator, and will be used in task 2 and 3 """

import itertools
import sys
import threading
import time
from functools import wraps

from matplotlib import pyplot as plt


def plot_histogram(func):
    # we can still get the original function attribute, like __name__
    @wraps(func)
    def wrap_function(*args, **kwargs):
        results = None

        # a new thread will run spinner, to killing time while waiting the result
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
        # stop spinner
        spinning.join()
        if len(results) != 0:
            plt.figure(figsize=(12, 10), dpi=300)
            plt.bar(list(x[0:20] for x in list(results.keys())), list(results.values()), 0.6, align='center')
            plt.title(func.__name__)
            print("\nAnalyzing data duration(s):", time.time() - start_time)

            start_time = time.time()
            plt.show()
            print("Plotting data duration(s):", time.time() - start_time)

    return wrap_function
