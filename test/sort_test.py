from algorithm.sort import insertion_sort, selection_sort, merge_sort, bubble_sort, fast_merge_sort, heap_sort, quicksort
import unittest
import numpy as np
from copy import deepcopy


class SortTest(unittest.TestCase):

    def setUp(self):
        self.arrays = []
        for size in (10, 100, 1000):
            self.arrays.append(np.random.randint(1000, size=size))

        self.printables = {1}

    def sort(self, sorting_algorithm):
        print(self)
        for i, test_array in enumerate(self.arrays, 1):
            array = deepcopy(test_array)  # copy it.
            ground_truth = sorted(array)
            if i in self.printables:
                print("Test Array:", test_array.tolist())
                print("Ground truth:", ground_truth)

            sorting_algorithm(test_array)

            if i in self.printables:
                print("Sorted Array:", test_array)
            diff = np.sum(np.abs(test_array - ground_truth))
            self.assertEqual(diff, 0)


class InsertionSortTest(SortTest):

    def test_sort(self):
        self.sort(insertion_sort)


class SelectionSortTest(SortTest):

    def test_sort(self):
        self.sort(selection_sort)


class MergeSort(SortTest):

    def test_sort(self):
        self.sort(merge_sort)


class FastMergeSort(SortTest):

    def test_sort(self):
        self.sort(fast_merge_sort)


class BubbleSort(SortTest):

    def test_sort(self):
        self.sort(bubble_sort)


class HeapSort(SortTest):

    def test_sort(self):
        self.sort(heap_sort)


class QuicksortTest(SortTest):

    def test_sort(self):
        self.sort(quicksort)
