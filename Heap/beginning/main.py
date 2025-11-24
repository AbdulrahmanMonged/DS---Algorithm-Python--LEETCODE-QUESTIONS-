class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def _left_child(self, index):
        return 2 * index

    def _right_child(self, index):
        return 2 * index + 1

    def _parent(self, index):
        return index // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _sink_down(self, index):
        pass
        #####
        

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 1 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def remove(self):
        if len(self.heap):
            if len(self.heap) == 1:
                return self.heap.pop()
            temp_val = self.heap[0]
            self.heap[1] = self.heap.pop()
            self._sink_down(1)
            return temp_val
        return None
    
            
            
            
            
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""
    