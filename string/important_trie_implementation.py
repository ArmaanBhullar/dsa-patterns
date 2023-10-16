"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""
class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        # start from root, go till prefix matches, then go on inserting till end of word
        node = self.root
        for char_ in word:
            if char_ in node.children:
                node = node.children[char_]
            else:
                # start inserting new nodes
                new_node = TrieNode(char_)
                node.children[char_] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char_ in word:
            if char_ in node.children:
                node = node.children[char_]
            else:
                return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char_ in prefix:
            if char_ in node.children:
                node = node.children[char_]
            else:
                return False
        return True


class TrieNode:

    def __init__(self, char_: str) -> None:
        self.char = char_
        self.children = {}  # key is char, value is TrieNode
        self.is_end = False  # marks end of word, can also be computed from children on the fly

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)