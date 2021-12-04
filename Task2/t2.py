#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task2 will use document ID """

import os
from Feed_ThreadPool import feed_json_threadpool
import pandas as pd
from Plot_Barchart import plot
from Nothing_exception import nothing_found_exception

def process_method(lock, userID, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read" and x.get("subject_doc_id", "") == docID, data)
    for dict in dicts:
        lock.acquire()
        result[dict.get("visitor_country")] = result.get(dict.get("visitor_country"), 0) + 1
        lock.release()


@plot.plot_histogram
@nothing_found_exception.exception
def view_by_country(docID, filename):
    """
    this actually equal to view_by_country = plot.plot_histogram(view_by_country)
    Time complexity: N
    Space complexity: N
    :param docID:
    :param filename:
    :return: A dictionary with country and counts
    """
    return feed_json_threadpool.feed_json_into_Threadpool(0, docID, filename, process_method)


@plot.plot_histogram
@nothing_found_exception.exception
def view_by_continent(docID, filename):
    """
    Here we use a external resource that contains the country ISO3166-2 code with it's continent
    Time complexity: N
    Space complexity: N
    """
    table = pd.read_csv(os.path.abspath(r"Task2/all.csv"))
    country_to_continent = table.set_index('alpha-2')['region'].to_dict()
    results = feed_json_threadpool.feed_json_into_Threadpool(0, docID, filename, process_method)
    new_results = {}
    # replace the country to continent
    for x in results:
        new_results[country_to_continent.get(x)] = results.get(x)
    del results
    return new_results


if __name__ == "__main__":
    view_by_continent("140218134226-85827c1f2cec7cde188f60901c23",
                      r"C:\Users\myper\Desktop\sample_3m_lines.json")
