import heapq

class MinHeap:
    def __init__(self, size = None):
        self.heap = []
        self.size = size

    def push(self, item, weight=None):
        if weight is not None:
            item = (-weight, item)
        heapq.heappush(self.heap, item)
        if self.size and len(self.heap) > self.size:
            res = self.pop()
        return None

    def pop(self):
        return heapq.heappop(self.heap)

    def ordered(self):
        return sorted(self.heap, reverse=True)


