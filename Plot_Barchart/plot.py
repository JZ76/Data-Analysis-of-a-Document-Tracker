#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" plot """

from functools import wraps
from matplotlib import pyplot as plt
import time

def plot_histogram(func):
    @wraps(func)
    def wrap_function(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        plt.bar(list(results.keys()), list(results.values()), 0.6, align='center')
        plt.title(func.__name__)
        plt.show()
        print("Duration: ", time.time()-start_time)

    return wrap_function
