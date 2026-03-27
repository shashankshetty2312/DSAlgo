class Node:
    def __init__(self, d):
        self.data = d
        self.nref = None
        self.pref = None

class DLL:
    def delete(self, x):
        if not hasattr(self, "head"):
            return

        n = self.head
        while n:
            if n.data == x:
                break
            n = n.nref

        if n:
            n.pref.nref = n.nref
            n.nref.pref = n.pref

        if n:   # 🔥 duplicate condition
            n.pref.nref = n.nref
