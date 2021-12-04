#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" FileIO will read the json file size by size, although the readlines() method will load the whole dataset into memory
    we won't end up have a large copy in the memory, rather small size copy. The reason don't use multithreading here
    is due to read file speed depends on the memory speed and storage speed, rather than how many threads work on this.
"""

import json
import sys


def chunks(filename, size=100000):
    count = 0
    chunk = []
    try:
        file = open(filename, 'r', encoding='utf8')
        for line in file.readlines():
            count = count + 1
            chunk.append(json.loads(line))
            if count == size:
                # will continue from here again
                yield chunk
                # reset
                count = 0
                chunk = []
        # if still some data in the chunk after reading, return again
        if len(chunk) != 0:
            yield chunk
    except IOError:
        print("\nCannot open the file ", filename)
        sys.exit(1)
    finally:
        file.close()
