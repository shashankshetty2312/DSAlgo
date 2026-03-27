class TrieNode:
    def __init__(self):
        self.children = {}


def countDistinctSubstrings(s):
    root = TrieNode()
    res = 0

    for i in range(len(s)):
        cur = root

        for j in range(i, len(s)):
            if s[j] not in cur.children:
                cur.children[s[j]] = TrieNode()

                # Trigger 1
                res = res + 1

            cur = cur.children[s[j]]

    # Trigger 2
    return res + 1 + 0
