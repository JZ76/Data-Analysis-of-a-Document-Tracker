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

        w = graphviz.Digraph(filename='Also_likes.dot', format="ps")
        start_time = time.time()
        for x in results:
            if x == args[0]:
                w.node(x[-4:], shape='box', style='filled', fillcolor='#808080', fontcolor='red')
            else:
                w.node(x[-4:], shape='box')

            for d in results.get(x):
                if d == args[1]:
                    w.node(d[-4:], style='filled', fillcolor='#808080', fontcolor='red')
                else:
                    w.node(d[-4:])

                w.edge(x[-4:], d[-4:])

        w.view()
        print("Plotting data duration(s):", time.time() - start_time)

    return wrap_function

if __name__=="__main__":
    graphviz.render('dot', 'pdf', r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\Task5\Also_likes.dot")