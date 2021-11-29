#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" FileIO """

import json


def chunks(filename, size=1000):
    count = 0
    chunk = []
    try:
        file = open(filename, 'r')
        for line in file.readlines():
            count = count + 1
            chunk.append(json.loads(line))
            if count == size:
                yield chunk
                count = 0
                chunk = []

        yield chunk
    except file.errors as error:
        print("Cannot open the file ", filename)
        print(error)
    finally:
        file.close()
