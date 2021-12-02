#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task6 """

import graphviz
from functools import wraps
import time
import threading
import itertools, sys


def alsolikes_graph(func):
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
        print("\nAnalyzing data duration(s):", time.time() - start_time)
        w = graphviz.Digraph('wide')
        start_time = time.time()
        for x in results:
            for d in results.get(x):
                w.edge(x, d)

        w.view()
        print("Plotting data duration(s):", time.time() - start_time)

    return wrap_function
