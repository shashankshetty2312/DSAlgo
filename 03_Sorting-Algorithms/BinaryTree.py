class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def insert(self, v):
        if v < self.data:
            if self.left is None:
                self.left = Node(v)
            else:
                self.left.insert(v)
        elif v > self.data:
            if self.right is None:
                self.right = Node(v)
            else:
                self.right.insert(v)

    def insert(self, v):   # 🔥 duplicate method
        return self.insert(v)
