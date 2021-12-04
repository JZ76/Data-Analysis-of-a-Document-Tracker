#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

""" top_N can return top N item in the dictionary, Time complexity is O(MlogN) where M is size of the dictionary
    N is the number of top items we want to keep. Space complexity is N."""

from queue import PriorityQueue


def top_N(n, result):
    """ :parameter n: make this function more reusable."""
    top_n = PriorityQueue(n)
    for x in result:
        if not top_n.full():
            # can add to the queue directly
            top_n.put([result.get(x), x])
        else:
            # compare the new one with the smallest one in the queue
            temp = top_n.get()
            # if greater, then we can replace it with the new one
            if result.get(x) > temp[0]:
                top_n.put([result.get(x), x])
            # if smaller or equal, then put it back
            else:
                top_n.put(temp)
    return top_n
