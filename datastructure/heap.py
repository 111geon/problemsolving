from cgitb import small


class heap:
    def __init__(self, ls=[]):
        self.data = ls

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insert_node(self, value):
        self.data.append(value)
        new_node_index = len(self.data) - 1

        while(new_node_index > 0 and self.data[self.parent_index(new_node_index)] > self.data[new_node_index]):
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            new_node_index = self.parent_index(new_node_index)

        return

    def pop_node(self):
        if len(self.data) == 1:
            return self.data.pop()

        result = self.data[0]
        self.data[0] = self.data.pop()
        trickle_node_index = 0

        smaller_child_index = self.get_smaller_child_index(trickle_node_index)
        while(smaller_child_index and self.data[smaller_child_index] < self.data[trickle_node_index]):
            self.data[smaller_child_index], self.data[trickle_node_index] = self.data[trickle_node_index], self.data[smaller_child_index]
            trickle_node_index = smaller_child_index
            smaller_child_index = self.get_smaller_child_index(trickle_node_index)

        return result

    def get_smaller_child_index(self, index):
        left_child_value = self.data[self.left_child_index(index)] if self.left_child_index(index) < len(self.data) else None
        right_child_value = self.data[self.right_child_index(index)] if self.right_child_index(index) < len(self.data) else None

        if left_child_value and right_child_value:
            return self.left_child_index(index) if left_child_value < right_child_value else self.right_child_index(index)

        elif left_child_value and not right_child_value:
            return self.left_child_index(index)

        else:
            return None
    
    @staticmethod
    def heapify(ls):
        for i in range(len(ls)//2-1, -1, -1):
            while True:
                smallest = i
                l = 2 * i + 1
                r = 2 * i + 2

                smallest = l if l < len(ls) and ls[l] < ls[smallest] else smallest
                smallest = r if r < len(ls) and ls[r] < ls[smallest] else smallest

                if smallest != i:
                    ls[i], ls[smallest] = ls[smallest], ls[i]
                    i = smallest
                else: break
        return

a = heap()
for i in [55,22,34,10,2,99,68]:
    a.insert_node(i)

b = []
while(a.data):
    b.append(a.pop_node())

import random
c = random.sample([i for i in range(10)], 10)
print(c)
heap.heapify(c)
print(c)
