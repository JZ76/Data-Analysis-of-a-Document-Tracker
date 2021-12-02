#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task5 """
from queue import PriorityQueue

from Feed_ThreadPool import feed_json_threadpool

user_set = set()


def process_method(lock, userID, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read", data)
    global user_set
    for dict in dicts:
        lock.acquire()
        if dict.get("subject_doc_id") == docID:
            user_set.add(dict.get("visitor_uuid"))
        if dict.get("visitor_uuid") in result:
            result.get(dict.get("visitor_uuid")).add(dict.get("subject_doc_id"))
        else:
            result[dict.get("visitor_uuid")] = {dict.get("subject_doc_id")}
        lock.release()


def top_10_alsoliked(docID, result):
    answer = []
    count = {}
    for x in result:
        for d in result.get(x):
            if d != docID:
                count[d] = count.get(d,0)+1
    top_10 = PriorityQueue(10)
    for x in count:
        if not top_10.full():
            top_10.put([count.get(x), x])
        else:
            temp = top_10.get()
            if count.get(x) > temp[0]:
                top_10.put([count.get(x), x])
            else:
                top_10.put(temp)
    while not top_10.empty():
        temp = top_10.get()
        answer.append(["Document ID:", temp[1], "\tNumber of readers:", temp[0]])
    return answer


def also_likes(userID, docID, filename, sort_func=top_10_alsoliked):
    global user_set
    results = feed_json_threadpool.feed_json_into_Threadpool(userID, docID, filename, process_method)
    if not (userID in user_set):
        print("Given user ID is not in the also likes user list, and will be ignored")
    new_results = {}
    for u in user_set:
        new_results[u] = results.get(u)
    del results
    list = sort_func(docID, new_results)
    print("Sorted liked documents: ")
    print(*list, sep="\n")


if __name__ == "__main__":
    also_likes(0, "140310171202-000000002e5a8ff1f577548fec708d50",
               r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_400k_lines.json")
