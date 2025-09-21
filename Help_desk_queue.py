# -------------------------
# Queue Class (Help Desk)
# -------------------------
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:  # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

    def peek(self):
        return self.front.value if self.front else None

    def print_queue(self):
        current = self.front
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("Queue (front → rear):", values if values else "Empty")