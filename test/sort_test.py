from algorithm.sort import insertion_sort
import unittest
import numpy as np


class SortTest(unittest.TestCase):

    def setUp(self):
        self.arrays = []
        for size in (10, 100, 1000):
            self.arrays.append(np.random.randint(-1000, 1000, size=[1, size]))

        self.printables = {1}


class InsertionSortTest(SortTest):

    def test_insertion_sort(self):
        for i, test_array in enumerate(self.arrays, 1):
            ground_truth = sorted(test_array)
            array = test_array[:]  # copy it.
            if i in self.printables:
                print "Test Array:", test_array
                print "Copy of the Test Array", array
                print "Ground truth:", ground_truth
            insertion_sort(array)
            diff = np.sum(ground_truth - array)
            self.assertEquals(diff, 0)





