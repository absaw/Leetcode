class TrieNode:
    def __init__(self):
        self.children = {} # key : character, value = TrieNode()
        self.lastWord = False
        self.word = None
class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.head
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.lastWord = True
        node.word = word

    def search(self, word: str) -> bool:
        # bad
        node = self.head
        def searchWord(node, pointer):
            
            for i in range(pointer,len(word)):
                ch = word[i]

                if ch == '.':
                    for child in node.children.values():
                        if searchWord(child, i+1):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.lastWord
        
        return searchWord(node,0)





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)