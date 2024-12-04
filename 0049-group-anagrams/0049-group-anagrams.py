class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaD = {}

        for word in strs:
            wordKey = [0]*26
            for ch in word:
                i = ord(ch) - ord('a')
                wordKey[i] += 1
            t = tuple(wordKey)
            if t in anaD:
                anaD[t].append(word)
            else:
                anaD[t] = [word]
        
        return list(anaD.values())