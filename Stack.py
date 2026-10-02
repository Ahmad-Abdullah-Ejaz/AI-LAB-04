# Task-01 : Implement Stack using Python Stack follows LIFO(Last in, first out) rule

class Stack:
    def __init__(self):
        self.items = []

# add items in list
    def push(self, item):
        self.items.append(item)
        print("Pushed:", item)

# remove top element of list
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None

        return self.items.pop()

#show top element of list

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None

        return self.items[-1]

#Check if list is empty or not

    def is_empty(self):
        return len(self.items) == 0

#Check size of list

    def size(self):
        return len(self.items)

#Display all list items

    def display(self):
        print("Stack:", self.items)

# Stack class Object is created

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())

print("Popped element:", s.pop())

s.display()
