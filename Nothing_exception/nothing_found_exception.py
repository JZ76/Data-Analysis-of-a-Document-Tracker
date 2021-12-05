#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import sys
from functools import wraps


class Salty_Exception(Exception):
    """check the length of name. """

    def __str__(self):
        return "Nothing found in this file!"


def exception(func):
    @wraps(func)
    def wrap_function(*args, **kwargs):
        results = {}
        try:
            results = func(*args, **kwargs)
            if len(results) == 0:
                raise Salty_Exception
        except Salty_Exception as e:
            print("\n", e, args[-1])
            sys.exit(1)
        finally:
            return results

    return wrap_function
