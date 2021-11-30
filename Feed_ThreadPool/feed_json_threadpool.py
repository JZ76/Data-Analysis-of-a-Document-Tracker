#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" * """

from FileIO import fileIO as fio
from ThreadPool import threadpool as tp


def feed_json_into_Threadpool(userID, docID, filename, process_method):
    result = {}
    for chunk in fio.chunks(filename):
        tp.threadpool_execute(docID, chunk, process_method, result)
    return result
