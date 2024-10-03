class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm=defaultdict(list)

        for s in strs:

            c=[0] * 26

            for char in s:
                i=ord(char)-ord("a")
                print(i)
                c[i]+=1
            
            hm[tuple(c)].append(s)
        
        return hm.values()