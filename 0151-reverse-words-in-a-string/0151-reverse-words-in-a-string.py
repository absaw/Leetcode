class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s_list = s.split(" ")
        print(s_list)
        result = ""
        for word in s_list[::-1]:
            if word.isalnum():
                result += word.strip() + " "
        return result[:-1]