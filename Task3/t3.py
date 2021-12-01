#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task3 """

from Feed_ThreadPool import feed_json_threadpool
from Plot_Barchart import plot
import re


def extract_browser(string):
    '''https://developer.mozilla.org/en-US/docs/Web/HTTP/Browser_detection_using_the_user_agent
    https://stackoverflow.com/questions/9847580/how-to-detect-safari-chrome-ie-firefox-and-opera-browser'''

    Opera = re.compile('Opera')
    Chrome = re.compile('Chrome')
    Chromium = re.compile('Chromium')
    Safari = re.compile('Safari')
    Firefox = re.compile('Firefox')
    IE = re.compile('MSIE')
    Seamonkey = re.compile('Seamonkey')

    if Opera.search(string):
        answer = "Opera"
    elif Chrome.search(string):
        answer = "Chrome"
    elif Chromium.search(string):
        answer = "Chromium"
    elif Safari.search(string):
        answer = "Safari"
    elif Firefox.search(string):
        answer = "Firefox"
    elif IE.search(string):
        answer = "IE"
    elif Seamonkey.search(string):
        answer = "Seamonkey"
    else:
        answer = "Other"
    return answer

def process_method_all(lock, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read", data)
    for dict in dicts:
        lock.acquire()
        result[dict.get("visitor_useragent")] = result.get(dict.get("visitor_useragent"), 0) + 1
        lock.release()


def process_method(lock, docID, data, result):
    dicts = filter(lambda x: x.get("event_type", "") == "read", data)
    for dict in dicts:
        lock.acquire()
        result[extract_browser(dict.get("visitor_useragent"))] = \
            result.get(extract_browser(dict.get("visitor_useragent")), 0) + 1
        lock.release()


@plot.plot_histogram
def view_by_browser_all(filename):
    results = feed_json_threadpool.feed_json_into_Threadpool(0, 0, filename, process_method_all)
    return results


@plot.plot_histogram
def view_by_browser(filename):
    results = feed_json_threadpool.feed_json_into_Threadpool(0, 0, filename, process_method)
    return results


if __name__ == "__main__":
    view_by_browser(
        r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_3m_lines.json")
