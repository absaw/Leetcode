class TrieNode:
    def __init__(self):
        self.children = {}
        self.LastWord = False

class Trie:

    def __init__(self):
        self.head = TrieNode()
        # return self.head

    def insert(self, word: str) -> None:
        # word="apple"
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.LastWord = True

    def search(self, word: str) -> bool:
        searchHead = self.head
        for c in word:
            if c in searchHead.children:
                searchHead = searchHead.children[c]
            else:
                return False
        return searchHead.LastWord
        # if searchHead.LastWord:
        #     return True
        # return False

    def startsWith(self, prefix: str) -> bool:
        searchHead = self.head
        for c in prefix:
            if c in searchHead.children:
                searchHead = searchHead.children[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)