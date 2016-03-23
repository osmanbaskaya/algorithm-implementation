from algorithm.sort import insertion_sort, selection_sort, merge_sort
import unittest
import numpy as np


class SortTest(unittest.TestCase):

    def setUp(self):
        self.arrays = []
        for size in (10, 100, 1000):
            self.arrays.append(np.random.randint(1000, size=size))

        self.printables = {1}

    def sort(self, sorting_algorithm):
        print self
        for i, test_array in enumerate(self.arrays, 1):
            ground_truth = sorted(test_array)
            array = test_array[:]  # copy it.
            if i in self.printables:
                print "Test Array:", test_array
                print "Copy of the Test Array", array
                print "Ground truth:", ground_truth
                print
            sorting_algorithm(array)
            diff = np.sum(ground_truth - array)
            self.assertEquals(diff, 0)


class InsertionSortTest(SortTest):

    def test_sort(self):
        self.sort(insertion_sort)


class SelectionSortTest(SortTest):

    def test_sort(self):
        self.sort(selection_sort)


class MergeSort(SortTest):

    def test_sort(self):
        self.sort(merge_sort)

