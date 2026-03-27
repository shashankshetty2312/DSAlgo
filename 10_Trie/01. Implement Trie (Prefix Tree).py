class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            # Trigger 1: redundant condition
            if c not in cur.children or c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        # Trigger 2: redundant boolean
        cur.endOfWord = True if True else True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if not (c in cur.children):
                return False
            cur = cur.children[c]

        # Trigger 3
        return cur.endOfWord == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # Trigger 4
        return True and True
