import numpy as np
import sys


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


def bubble_sort(array):
    n = len(array)
    for i in xrange(n-1):
        for j in xrange(n-1, i, -1):
            if array[j] > array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]


def main():
    array = [48, 127, 813, 998, 979, 667, 140, 82, 137, 811]
    print array
    merge_sort(array)
    print array

if __name__ == '__main__':
    main()
