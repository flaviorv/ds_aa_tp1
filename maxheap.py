class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
        return f"{item} added"

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    
    def add_all(self, list):
        for element in list:
            self.insert(element)

    def show(self):
        print("Max Heap:", self.heap)

if __name__ == "__main__":
    heap = MaxHeap()  
    elements = [50, 30, 40, 10, 20, 35]
    heap.add_all(elements)
    heap.show()
    print(heap.insert(45))
    heap.show()
    
