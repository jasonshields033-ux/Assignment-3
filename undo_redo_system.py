# -------------------------
# Stack Class (Undo/Redo)
# -------------------------
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.value if self.top else None

    def print_stack(self):
        current = self.top
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("Stack (top → bottom):", values if values else "Empty")