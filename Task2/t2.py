#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task2 """

import os
from Feed_ThreadPool import feed_json_threadpool
import pandas as pd
from Plot_Barchart import plot


def process_method(lock, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read" and x.get("subject_doc_id", "") == docID, data)
    for dict in dicts:
        lock.acquire()
        result[dict.get("visitor_country")] = result.get(dict.get("visitor_country"), 0) + 1
        lock.release()


@plot.plot_histogram
def view_by_country(docID, filename):
    results = feed_json_threadpool.feed_json_into_Threadpool(0, docID, filename, process_method)
    return results


@plot.plot_histogram
def view_by_continent(docID, filename):
    table = pd.read_csv(os.path.abspath(r"all.csv"))
    country_to_continent = table.set_index('alpha-2')['region'].to_dict()
    results = feed_json_threadpool.feed_json_into_Threadpool(0, docID, filename, process_method)
    new_results = {}
    for x in results:
        new_results[country_to_continent.get(x)] = results.get(x)
    del results
    return new_results


if __name__ == "__main__":
    view_by_continent("140218134226-85827c1f2cec7cde188f60901c23558d",
                      r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\issuu_cw2.json")
