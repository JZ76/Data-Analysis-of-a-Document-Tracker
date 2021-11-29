#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" task2 """

import json
from FileIO import fileIO as fio

def read_json(*args):
    doc_id = args[1]
    fio.chunks("issuu_cw2.json")
