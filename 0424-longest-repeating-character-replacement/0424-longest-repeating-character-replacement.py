class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0  # Left pointer of the window
        maxLen = 0  # Result to store the maximum length
        charMap = {}  # Dictionary to count characters in the current window
        
        for r in range(len(s)):
            # Update the frequency of the character at the right pointer
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            
            # Calculate the window length and the most frequent character count
            windowLen = r - l + 1
            mostFrequentChar = max(charMap.values())
            changesNeeded = windowLen - mostFrequentChar
            
            # If changes exceed k, shrink the window from the left
            if changesNeeded > k:
                charMap[s[l]] -= 1
                if charMap[s[l]] == 0:
                    del charMap[s[l]]  # Clean up the dictionary
                l += 1  # Move left pointer to the right
            else:
                # Update the maximum length if within k replacements
                maxLen = max(maxLen, windowLen)
        
        return maxLen