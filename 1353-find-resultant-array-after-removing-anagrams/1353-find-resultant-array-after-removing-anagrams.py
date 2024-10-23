'''
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    if s == t:
        return True
    s_idx = [0]*26
    t_idx = [0]*26
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        ordinal1 = ord(c1)-ord('a')
        ordinal2 = ord(c2) - ord('a')
        s_idx[ordinal1] += 1
        t_idx[ordinal2] += 1
    if s_idx==t_idx:
        return True
i = len(words)-1
while i > 0 :
    #curr_ana = [0]*26
    if isAnagram(words[i],words[i-1]):
        words.pop(i)
        
    i-=1
return words


'''

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s,t):
            if len(s)!=len(t):
                return False
            if s == t:
                return True
            s_idx = [0]*26
            t_idx = [0]*26
            for i in range(len(s)):
                c1 = s[i]
                c2 = t[i]
                ordinal1 = ord(c1)-ord('a')
                ordinal2 = ord(c2) - ord('a')
                s_idx[ordinal1] += 1
                t_idx[ordinal2] += 1
            if s_idx==t_idx:
                return True
        i = len(words)-1
        while i > 0 :
            #curr_ana = [0]*26
            if isAnagram(words[i],words[i-1]):
                words.pop(i)
            i-=1
        return words