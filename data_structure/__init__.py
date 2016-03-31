class Heap(object):

    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)
        self.__build_heap()

    def __build_heap(self):
        for i in xrange(self.heap_size / 2, -1, -1):
            self.max_heapify(i)

    def left(self, index):
        i = (index+1) * 2 - 1
        return None if len(self.array) <= i else i

    def right(self, index):
        i = (index+1) * 2
        return None if len(self.array) <= i else i

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        print i, left, right, len(self.array)
        if left is not None and self.array[left] > self.array[i]:
            m = left
        else:
            m = i
        if right is not None and self.array[right] > self.array[m]:
            m = right

        self.array[m], self.array[i] = self.array[i], self.array[m]
        if m != i:
            self.max_heapify(m)

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return str(self.array)

