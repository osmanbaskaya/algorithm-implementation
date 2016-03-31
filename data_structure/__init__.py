class Heap(object):

    def __init__(self, array, heap_type='max'):
        self.array = array
        self.heap_size = len(array)

        if heap_type != 'max' and heap_type != 'min':
            raise AttributeError("Min or max")

        self.heap_type = heap_type
        if self.heap_type == 'max':
            heapify = self.max_heapify
        elif self.heap_type == 'min':
            heapify = self.min_heapify

        self.heapify = heapify
        self.__build_heap()

    def __build_heap(self):
        for i in xrange(self.heap_size / 2, -1, -1):
            self.heapify(i)

    def left(self, index):
        i = (index+1) * 2 - 1
        return None if self.heap_size <= i else i

    def right(self, index):
        i = (index+1) * 2
        return None if self.heap_size <= i else i

    def min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left is not None and self.array[left] < self.array[i]:
            m = left
        else:
            m = i
        if right is not None and self.array[right] < self.array[m]:
            m = right

        self.array[m], self.array[i] = self.array[i], self.array[m]
        if m != i:
            self.heapify(m)

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left is not None and self.array[left] > self.array[i]:
            m = left
        else:
            m = i
        if right is not None and self.array[right] > self.array[m]:
            m = right

        self.array[m], self.array[i] = self.array[i], self.array[m]
        if m != i:
            self.heapify(m)

    def heapsort(self):
        while self.heap_size != 1:
            self.array[0], self.array[self.heap_size-1] = self.array[self.heap_size-1], self.array[0]
            self.heap_size -= 1
            self.heapify(0)

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return str(self.array)
