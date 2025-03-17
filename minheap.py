from random import randrange
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, person):
        print(f"Adding {person["priority"]}")
        self.heap.append(person)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index]["priority"] < self.heap[parent_index]["priority"]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def insert_queue(self, queue):
        for person in queue:
            self.insert(person)

    def show(self, type=None):
        print("Min Heap:", end=" ")
        if type == "priority" or type == "person":
            for i in self.heap:
                print(i[type], end=" ")
            print()
        else:
            print(self.heap)

    def pop(self):
        if len(self.heap) == 0:
            print("There is nothing to remove")
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        print(f"Root {root} removed")
        return root

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child]["priority"] < self.heap[smallest]["priority"]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child]["priority"] < self.heap[smallest]["priority"]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def show_root(self):
        print(f"The root is {self.heap[0]}")

if __name__ == "__main__":
    queue = [
        {"priority": 5, "person": "Amanda"},
        {"priority": 2, "person": "Bruno"},
        {"priority": 3, "person": "Carlos"},
        {"priority": 7, "person": "Daniela"},
        {"priority": 1, "person": "Eduardo"},
    ]

    heap = MinHeap()
    heap.insert_queue(queue)
    heap.show("priority")
    heap.show_root()
    heap.insert({"priority": 0, "person": "João"})
    heap.show_root()
    print(heap.pop())
    heap.show_root()
    print(heap.pop())
    heap.show_root()
