#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task5 """

from queue import PriorityQueue
from Task6.t6 import alsolikes_graph
from Feed_ThreadPool import feed_json_threadpool

user_set = set()
temp_display = ""

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
                count[d] = count.get(d, 0) + 1
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
    i = top_10.qsize()
    while not top_10.empty():
        temp = top_10.get()
        answer.append("Ranking:" + str(i) + "\tDocument ID: " + temp[1] + "\tNumber of readers: " + str(temp[0]))
        i = i - 1
    return answer


def also_likes(userID, docID, filename):
    global user_set
    global temp_display
    results = feed_json_threadpool.feed_json_into_Threadpool(userID, docID, filename, process_method)
    if not (userID in user_set):
        temp_display = "Given user ID is not in the also likes user list, and will be ignored\n"
        print(temp_display)
    new_results = {}
    for u in user_set:
        new_results[u] = results.get(u)
    del results
    user_set = set()
    return new_results


def alsolikes_sorted(userID, docID, filename, sort_func=top_10_alsoliked):
    global temp_display
    new_results = also_likes(userID, docID, filename)
    list = sort_func(docID, new_results)
    string_display = temp_display
    temp_display = ""
    string_display = string_display + "Sorted liked documents: \n"
    string_display = string_display + "\n".join(str(x) for x in list)
    print(string_display)
    return string_display


@alsolikes_graph
def generate_graph(userID, docID, filename):
    return also_likes(userID, docID, filename)

if __name__ == "__main__":
    alsolikes_sorted("4065369dbee2b902", "140310170010-0000000067dc80801f1df696ae52862b",
               r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_400k_lines.json")
