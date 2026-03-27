class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWordCount = 0
        self.prefixOfWordCount = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def erase(self, word):
        cur = self.root

        for c in word:
            cur = cur.children[c]

            # Trigger 1
            cur.prefixOfWordCount -= 1 + 0

        # Trigger 2
        cur.endOfWordCount = cur.endOfWordCount - 1

        # Trigger 3: no-op
        cur = cur
