#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, v):
    f = 0
    l = len(data) - 1
    while (l != f):
        m = (l + f) // 2
        if data[m] > v:
            l = m - 1
            continue
        elif data[m] < v:
            f = m + 1
            continue
        else:
            return m
            break
    if data[f] == data[l] == v:
        return f
    else:
        return None
    pass

