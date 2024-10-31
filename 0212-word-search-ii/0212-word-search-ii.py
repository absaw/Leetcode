from typing import List, Set

class TrieNode:
    def __init__(self):
        self.children = {}
        self.lastWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def addWord(self, word):
        node = self.head
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
        node.lastWord = True

    def deleteWord(self, word):
        # Helper function to delete a word from the Trie and prune dead nodes
        def delete(node, word, depth):
            if depth == len(word):
                node.lastWord = False
                node.word = None
            else:
                ch = word[depth]
                child_node = node.children.get(ch)
                if child_node and delete(child_node, word, depth + 1):
                    del node.children[ch]
            return not node.children and not node.lastWord

        delete(self.head, word, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Add all words to the Trie
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        M, N = len(board), len(board[0])
        res = set()
        path: Set[tuple] = set()
        
        def dfs(r, c, node):
            # Base case to exit DFS if conditions aren't met
            if (r not in range(M) or c not in range(N) or 
                board[r][c] not in node.children or
                (r, c) in path):
                return
            
            ch = board[r][c]
            node = node.children[ch]
            
            # If a word is found, add it to the result and remove from Trie
            if node.lastWord:
                res.add(node.word)
                trie.deleteWord(node.word)  # Remove word to avoid revisits
            
            # DFS on adjacent cells
            path.add((r, c))
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            path.remove((r, c))
        
        # Start DFS from every cell
        for r in range(M):
            for c in range(N):
                dfs(r, c, trie.head)
        
        return list(res)