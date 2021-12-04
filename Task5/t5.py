#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task5 will use Document ID and User ID, but user ID is optional"""

from TopN import topn
from Task6.t6 import alsolikes_graph
from Feed_ThreadPool import feed_json_threadpool

# shared by all threads and methods
user_set = set()
temp_display = ""


def process_method(lock, userID, docID, data, result):
    """
    Two things to record, one is a dictionary that store every users' read list, one user will map to one or more doc.
    Another is a user list that store the user have read the given docID.
    """
    dicts = filter(lambda x: x.get("event_type", "") == "read", data)
    global user_set
    for dic in dicts:
        lock.acquire()
        # user list will use set to prevent duplicated userID
        if dic.get("subject_doc_id") == docID:
            user_set.add(dic.get("visitor_uuid"))
        if dic.get("visitor_uuid") in result:
            # if the docID already in the user read list, do nothing
            result.get(dic.get("visitor_uuid")).add(dic.get("subject_doc_id"))
        else:
            # creat a new set, and put in the new docID
            result[dic.get("visitor_uuid")] = {dic.get("subject_doc_id")}
        lock.release()


def top_10_alsoliked(userID, docID, result):
    answer = []
    count = {}
    # count how many a document read by users in the result
    if not (userID in result):
        for x in result:
            for d in result.get(x):
                count[d] = count.get(d, 0) + 1
    else:
        del result[userID]
        for x in result:
            for d in result.get(x):
                if d != docID:
                    count[d] = count.get(d, 0) + 1
    top_10 = topn.top_N(10, count)
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
    new_results = {}
    # get the users that read docID
    for u in user_set:
        new_results[u] = results.get(u)
    del results
    # reset, otherwise still store the result and rise error in GUI
    user_set = set()
    # conner case
    if len(new_results) == 0:
        temp_display = temp_display + "There is no user read this document " + docID + " in the file " + filename + "\n"
    elif len(new_results) == 1:
        temp_display = temp_display + "There is only one user read this document!\n"
    return new_results


def alsolikes_sorted(userID, docID, filename, sort_func=top_10_alsoliked):
    """
    Time complexity: depends on the sorting function
    Space complexity: depends on the sorting function
    """
    global temp_display
    print("Start analyzing data...")
    new_results = also_likes(userID, docID, filename)
    string_display = temp_display
    temp_display = ""
    string_display = "Task 5:\n" + string_display
    if len(new_results) > 0:
        # apply sorting algorithm to the result
        list = sort_func(userID, docID, new_results)
        string_display = string_display + "Sorted also liked documents: \n"
        string_display = string_display + "\n".join(str(x) for x in list)
    print(string_display)
    return string_display


@alsolikes_graph
def generate_graph(userID, docID, filename):
    """
    This is Task6, but we have to use also_likes function from Task5, so, we put part of task6 function here
    Time complexity: N
    Space complexity: N
    """
    global temp_display
    t = also_likes(userID, docID, filename)
    print(temp_display)
    temp_display = ""
    return t


if __name__ == "__main__":
    alsolikes_sorted('97c0363c52a07020', "140109173556-a4b921ab7619621709b098aa9de4d736",
                   r"C:\Users\myper\Desktop\sample_3m_lines.json")
