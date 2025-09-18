"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        size = len(s)
        if size == 1: return 1
    
        lp = 0
        rp = 1
        maxlen = 1

        seen = set(s[lp])
        seen.add(s[lp])
        while lp < rp and rp < size:
            length = 0
            if s[rp] in seen:
                while s[lp] != s[rp]:
                    seen.remove(s[lp])
                    lp+=1
                lp+=1                
            seen.add(s[rp])            
            length = rp - lp + 1
            maxlen = max(maxlen, length)
            rp += 1

        return maxlen


