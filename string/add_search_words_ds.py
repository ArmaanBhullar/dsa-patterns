"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
"""
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.word_flat_set = set()

    def addWord(self, word: str) -> None:
        if word not in self.word_flat_set:
            node = self.root
            for char in word:
                if char in node.children:
                    node = node.children[char]
                else:
                    new_node = TrieNode(char)
                    node.children[char] = new_node
                    node = new_node
            node.is_end = True
            self.word_flat_set.add(word)

    def search(self, word: str) -> bool:
        if "." in word:
            self.results = []
            ls = [(self.root, 0)]
            while len(ls) > 0:
                node, word_idx = ls.pop()
                if word_idx == len(word):
                    if node.is_end:
                        return True
                else:
                    if word[word_idx] == '.':
                        # put all children in ls
                        for neighbor in node.children.values():
                            ls.append((neighbor, word_idx + 1))
                    else:
                        if word[word_idx] in node.children:
                            ls.append((node.children[word[word_idx]], word_idx + 1))
            return False
        else:
            return word in self.word_flat_set


class TrieNode:

    def __init__(self, char: str = ""):
        self.char = char
        self.children = {}
        self.is_end = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)