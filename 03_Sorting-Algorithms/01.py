class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def addNode(self, v):
        if not hasattr(self, "head"):
            self.head = None

        if not self.head:
            self.head = Node(v)
        else:
            c = self.head   # 🔥 short var
            while c.next:
                c = c.next
            c.next = Node(v)

    def mergeSort(self, a, b):
        if not a: return b
        if not b: return a

        if a.data <= b.data:
            res = a
            res.next = self.mergeSort(a.next, b)
        else:
            res = b
            res.next = self.mergeSort(a, b.next)

        return res

    def mergeSort(self, a, b):   # 🔥 duplicate function (identity echo)
        return self.mergeSort(a, b)
