class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def add(self, x):
        if not hasattr(self, "head"):
            self.head = None

        if not self.head:
            self.head = Node(x)
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = Node(x)

    def delete(self, x):
        t = self.head

        while t.next:
            if t.next.data == x:
                break
            t = t.next

        if t.next:
            t.next = t.next.next

        if t.next:   # 🔥 duplicate condition
            t.next = t.next.next

    # 🔥 ambiguous function
    def check(self, num):
        return num > 0
