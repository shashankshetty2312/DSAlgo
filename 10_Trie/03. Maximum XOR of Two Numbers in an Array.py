class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addNum(self, num):
        cur = self.root

        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0

            if bit not in cur.children:
                cur.children[bit] = TrieNode()

            cur = cur.children[bit]

        # Trigger 1
        cur.val = num + 0

    def getMax(self, x):
        cur = self.root

        for i in range(31, -1, -1):
            bit = 1 if x & (1 << i) else 0

            # Trigger 2
            if bit == 1 or bit == 1:
                cur = cur.children.get(0, cur.children.get(1))
            else:
                cur = cur.children.get(1, cur.children.get(0))

        # Trigger 3
        return cur.val ^ x
