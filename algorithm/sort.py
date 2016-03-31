import numpy as np
import sys
import math


def insertion_sort(array):
    """
    In-place insertion sort
    """

    length = len(array)
    for i in xrange(1, length):
        # [i-1, i-2, ..., 0]
        index = i
        e = array[index]
        for j in xrange(i-1, -1, -1):
            if array[j] > e:
                # swap
                array[index], array[j] = array[j], array[index]
                index = j
            else:
                break


def insertion_sort_recursive(array):

    if len(array) > 1:
        last_elem = array[-1]
        arr = insertion_sort_recursive(array[:-1])
        arr.append(last_elem)
        index = len(arr) - 1
        for i in xrange(len(arr)-2, -1, -1):
            if arr[i] > last_elem:
                arr[index], arr[i] = arr[i], arr[index]
                index = i
            else:
                break
    else:
        arr = array

    return arr


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


def merge(array, p, q, r):
    left = array[p:q]
    left.append(sys.maxint)
    right = array[q:r]
    right.append(sys.maxint)

    left_index = 0
    right_index = 0
    for k in xrange(p, r):
        if left[left_index] < right[right_index]:
            array[k] = left[left_index]
            left_index += 1
        else:
            array[k] = right[right_index]
            right_index += 1


def merge_sort(array, p=None, r=None):

    if isinstance(array, np.ndarray):
        array = array.tolist()

    if p is None:
        p = 0
    if r is None:
        r = len(array)

    if r - p > 1:
        q = (r + p) / 2
        merge_sort(array, p, q)
        merge_sort(array, q, r)
        merge(array, p, q, r)


def fast_merge_sort(array, p=None, r=None):

    if isinstance(array, np.ndarray):
        array = array.tolist()

    if p is None:
        p = 0
    if r is None:
        r = len(array)

    k = int(math.log(len(array)))

    if r - p <= k:
        arr = array[p:r]
        insertion_sort(arr)
        array[p:r] = arr
    else:
        if r - p > 1:
            q = (r + p) / 2
            merge_sort(array, p, q)
            merge_sort(array, q, r)
            merge(array, p, q, r)


def bubble_sort(array):
    n = len(array)
    for i in xrange(n-1):
        for j in xrange(n-1, i, -1):
            if array[j] > array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]


def main():
    array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    from data_structure import Heap
    h = Heap(array)
    print h
    h.heapsort()
    print h


if __name__ == '__main__':
    main()
