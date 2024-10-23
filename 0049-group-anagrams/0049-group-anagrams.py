'''
idx_anagram_array = [0]*26
for str in strs:
for c in str:
    i = ord('c')-ord('a')
    idx_anagram_array[i] += 1
dict[tuple(idx_anagram_array)]+=1
return dict.values() 
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for s in strs:
            idx_anagram_array = [0]*26
            for c in s:
                i = ord(c)-ord('a')
                idx_anagram_array[i] += 1
            dct[tuple(idx_anagram_array)].append(s)
        # print(list(dct.values()))
        return list(dct.values())