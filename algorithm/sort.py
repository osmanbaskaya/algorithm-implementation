import numpy as np


def insertion_sort(array):
    """
    In-place insertion sort
    """

    def swap(index1, index2):
        tmp = array[index1]
        array[index1] = array[index2]
        array[index2] = tmp

    length = len(array)
    for i in xrange(1, length):
        # [i-1, i-2, ..., 0]
        index = i
        e = array[index]
        for j in xrange(i-1, -1, -1):
            if array[j] > e:
                swap(j, index)
                index = j
            else:
                break


def selection_sort(array):
    length = len(array)
    for i in xrange(length-1):
        min_val, min_index = array[i], i
        for j in xrange(i+1, length):
            if min_val > array[j]:
                min_val = array[j]
                min_index = j
        # swap
        array[i], array[min_index] = array[min_index], array[i]


