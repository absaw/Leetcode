#  l e e t c o d e
#i         4

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordIndex = [False] * (len(s)+1)
        wordIndex[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):

            for word in wordDict:

                if i+len(word)<=len(s) and s[i:i+len(word)] == word:
                    wordIndex[i] = wordIndex[i+len(word)]
                
                if wordIndex[i]:
                    break
        
        return wordIndex[0]