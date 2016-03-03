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


if __name__ == '__main__':
    a = [-1, 45,2,1,2,58,5]
    a = np.array(a)
    insertion_sort(a)
    print a
    a = a[::-1]
    print a
    insertion_sort(a)
    print a



