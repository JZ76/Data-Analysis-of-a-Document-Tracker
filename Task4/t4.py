#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task4 will focus on "event_type":"pagereadtime" """

from Feed_ThreadPool import feed_json_threadpool
from TopN import topn
import time


def process_method(lock, userID, docID, data, result):
    """ this time we will find pagereadtime event rather than read event."""
    dicts = filter(lambda x: x.get("event_type", "") == "pagereadtime", data)
    for dict in dicts:
        lock.acquire()
        result[dict.get("visitor_uuid")] = result.get(dict.get("visitor_uuid"), 0) + dict.get("event_readtime")
        lock.release()


def top_10_reader(filename):
    """
    If the size of data much greater than the top number of items we want, this sorting function will become linear
    time complexity
    Time complexity: Nlog10
    Space complexity: 10
    """
    print("Start analyzing data...")
    start_time = time.time()
    result = feed_json_threadpool.feed_json_into_Threadpool(0, 0, filename, process_method)
    print("\nAnalyzing data duration(s):", time.time() - start_time)
    start_time = time.time()
    string_display = "Task4:\n"
    if len(result) == 0:
        string_display = string_display + "Not found any readers in the file" + filename
    top_10 = topn.top_N(10, result)
    i = top_10.qsize()
    while not top_10.empty():
        temp = top_10.get()
        string_display = string_display + ("Ranking:" + str(i) + "\tUser:" + temp[1] + "\tReading time (mins):" + str(temp[0]/60000))
        string_display = string_display + "\n"
        i = i - 1
    print(string_display)
    # usually the sorting time will less than 1s
    print("Sorting data duration(s):", time.time() - start_time)
    return string_display


if __name__ == "__main__":
    top_10_reader(r"C:\Users\myper\Desktop\sample_400k_lines.json")
