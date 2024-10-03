class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_set = set()
        anagram_dict = {}

        for word in strs:

            sorted_word = tuple(sorted(word))
            # print(sorted_word)
            if sorted_word not in anagram_set:
                anagram_set.add(sorted_word)
                anagram_dict[sorted_word] = [word]

            else:
                anagram_dict[sorted_word].append(word)
        
        return anagram_dict.values()