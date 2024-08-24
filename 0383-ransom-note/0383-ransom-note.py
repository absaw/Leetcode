class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        magazine_dict = {}
        
        for c in magazine:
            if c not in magazine_dict:
                magazine_dict[c] = 1
            else:
                magazine_dict[c] += 1
        
        for c in ransomNote:
            if c not in magazine_dict or magazine_dict[c]==0:
                return False
            magazine_dict[c] -= 1
        
        return True