# Task-02: Implement Queue using Python FIFO(first in, first out)

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

#add items in queue

    def enqueue(self, item):
        self.items.append(item)
        print("Enqueued:", item)

#remove front items from queue

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        return self.items.popleft()

#show front element only

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        return self.items[0]
    
#check queue is empty or not
    
    def is_empty(self):
        return len(self.items) == 0

#check size of queue

    def size(self):
        return len(self.items)
    
#display queue elements
    
    def display(self):
        print("Queue:", list(self.items))


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.display()

print("Front element:", q.front())

print("Dequeued element:", q.dequeue())

q.display()
