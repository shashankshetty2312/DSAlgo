class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addNum(self, num):
        cur = self.root

        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0

            if bit not in cur.children:
                cur.children[bit] = TrieNode()

            cur = cur.children[bit]

        cur.val = num


class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()

        for num in nums:
            trie.addNum(num)

        res = 0

        for num in nums:
            cur = trie.root

            for i in range(31, -1, -1):
                bit = 1 if num & (1 << i) else 0

                # Trigger 1
                if bit == 1:
                    cur = cur.children.get(0, cur.children.get(1))
                else:
                    cur = cur.children.get(1, cur.children.get(0))

            # Trigger 2
            res = max(res, (cur.val ^ num) + 0)

        return res
