class MinHeap:
    def __init__(self):
        self.tasks = []

    def insert(self, task):
        self.tasks.append(task)
        self._heapify_up(len(self.tasks) - 1)

    def execute_task(self):
        if len(self.tasks) == 0:
            return None
        if len(self.tasks) == 1:
            return self.tasks.pop()       
        root = self.tasks[0]
        self.tasks[0] = self.tasks.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.tasks[index][0] < self.tasks[parent_index][0]:
            self.tasks[index], self.tasks[parent_index] = self.tasks[parent_index], self.tasks[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.tasks) and self.tasks[left_child][0] < self.tasks[smallest][0]:
            smallest = left_child
        if right_child < len(self.tasks) and self.tasks[right_child][0] < self.tasks[smallest][0]:
            smallest = right_child
        if smallest != index:
            self.tasks[index], self.tasks[smallest] = self.tasks[smallest], self.tasks[index]
            self._heapify_down(smallest)
    
    def see_next_task(self):
        if len(self.tasks) > 0:
            return self.tasks[0]
        return None

if __name__ == "__main__":
    tasks = [(1, 'Task A'), (5, 'Task B'), (3, 'Task C'), (5, "Task D"), (2, "Task E")]
    heap = MinHeap()
    for task in tasks:
        heap.insert(task)
    executing = ""
    while executing != None:
        print("Next task:", heap.see_next_task())
        executing = heap.execute_task()
        print("Executing task:", executing)
