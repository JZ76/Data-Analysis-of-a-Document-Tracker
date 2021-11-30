#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task4 """

from FileIO import fileIO as fio
from ThreadPool import threadpool as tp
from queue import PriorityQueue
import time


def process_method(userID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "pagereadtime", data)
    for dict in dicts:
        result[dict.get("visitor_uuid")] = result.get(dict.get("visitor_uuid"), 0) + dict.get("event_readtime")


def feed_json_into_Threadpool(userID, docID, filename):
    result = {}
    for chunk in fio.chunks(filename):
        tp.threadpool_execute(docID=docID, dataset=chunk, func=process_method, result=result)
    return result


def top_10_reader(userID, docID, filename):
    start_time = time.time()
    result = feed_json_into_Threadpool(userID, docID, filename)
    print(time.time() - start_time)
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
    while not top_10.empty():
        print(top_10.get())



if __name__ == "__main__":
    top_10_reader(0,
                  0,
                  r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_400k_lines.json")
