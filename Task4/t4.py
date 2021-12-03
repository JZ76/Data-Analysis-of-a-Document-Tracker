#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task4 """

from Feed_ThreadPool import feed_json_threadpool
from queue import PriorityQueue
import time


def process_method(lock, userID, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "pagereadtime", data)
    for dict in dicts:
        lock.acquire()
        result[dict.get("visitor_uuid")] = result.get(dict.get("visitor_uuid"), 0) + dict.get("event_readtime")
        lock.release()


def top_10_reader(filename):
    start_time = time.time()
    result = feed_json_threadpool.feed_json_into_Threadpool(0, 0, filename, process_method)
    print("\nAnalyzing data duration(s):", time.time() - start_time)
    start_time = time.time()
    top_10 = PriorityQueue(10)
    for x in result:
        if not top_10.full():
            top_10.put([result.get(x), x])
        else:
            temp = top_10.get()
            if result.get(x) > temp[0]:
                top_10.put([result.get(x), x])
            else:
                top_10.put(temp)
    string_display = "Task4:\n"
    i = top_10.qsize()
    if i == 0:
        string_display = string_display + "Not found any readers in the file" + filename
    while not top_10.empty():
        temp = top_10.get()
        print("Ranking:", str(i), "\tUser:", temp[1], "\tReading time (mins):", temp[0]/60000)
        string_display = string_display + ("Ranking:" + str(i) + "\tUser:" + temp[1] + "\tReading time (mins):" + str(temp[0]/60000))
        string_display = string_display + "\n"
        i = i - 1
    print("Sorting data duration(s):", time.time() - start_time)
    return string_display


if __name__ == "__main__":
    top_10_reader(r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_400k_lines.json")
