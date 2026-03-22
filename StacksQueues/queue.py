class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return True if self.count == 0 else False

    def enqueue(self, item):
        if self.is_full():
            print("Queue is already full!")
            return None
        self.rear += 1
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is already empty!")
            return None
        item_removed = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.count -= 1
        return item_removed

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        print(self.queue)

    
# Test Code
queue1 = Queue(5)

# Read input numbers (e.g. 10 20 30)
numbers = list(map(int, input().split()))

# Enqueue the numbers
for num in numbers:
    queue1.enqueue(num)

# Display the queue
queue1.display()

# Remove one element
print(f"Item removed: {queue1.dequeue()}")

# Display the queue again
queue1.display()