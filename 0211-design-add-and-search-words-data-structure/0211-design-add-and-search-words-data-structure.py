class TrieNode:
    def __init__(self):
        self.children = {}
        self.last_word = False
class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.last_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.last_word
        return dfs(0,self.head)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)