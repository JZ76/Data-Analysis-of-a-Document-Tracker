#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task2 """
import os
from functools import wraps

from FileIO import fileIO as fio
from ThreadPool import threadpool as tp
import pandas as pd
from matplotlib import pyplot as plt

def plot_histogram(func):
    @wraps(func)
    def wrap_function(*args, **kwargs):
        results = func(*args, **kwargs)
        plt.bar(list(results.keys()), list(results.values()), 0.6, align='center')
        plt.title('Views by country')
        plt.ylabel('Counts')
        plt.xlabel('countries')
        plt.show()

    return wrap_function

def process_method(docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read" and x.get("subject_doc_id", "") == docID, data)
    for dict in dicts:
        result[dict.get("visitor_country")] = result.get(dict.get("visitor_country"), 0) + 1

def feed_json_into_Threadpool(userID, docID, filename):
    result = {}
    for chunk in fio.chunks(filename):
        tp.threadpool_execute(docID, chunk, process_method, result)
    return result

@ plot_histogram
def view_by_country(userID, docID, filename):
    results = feed_json_into_Threadpool(userID, docID, filename)
    return results

@ plot_histogram
def view_by_continent(userID, docID, filename):
    table = pd.read_csv(os.path.abspath(r"Task2\all.csv"))
    country_to_continent = table.set_index('alpha-2')['region'].to_dict()
    results = feed_json_into_Threadpool(userID, docID, filename)
    new_results = {}
    for x in results:
        new_results[country_to_continent.get(x)] = results.get(x)
    del results
    return new_results

if __name__ == "__main__":
    view_by_continent(0, "140222150808-00000000c5cc18fc5b49993a2f7edf92", r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\issuu_cw2.json")