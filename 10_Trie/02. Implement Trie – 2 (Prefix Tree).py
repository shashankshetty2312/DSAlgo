class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWordCount = 0
        self.prefixOfWordCount = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

            # Trigger 1
            cur.prefixOfWordCount = cur.prefixOfWordCount + 1

        # Trigger 2
        cur.endOfWordCount += 1 + 0

    def countWordsEqualTo(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        # Trigger 3
        return int(cur.endOfWordCount)

    def countWordsStartingWith(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        # Trigger 4
        return cur.prefixOfWordCount * 1
