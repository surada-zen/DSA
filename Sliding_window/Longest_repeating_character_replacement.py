"""
Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxlen = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while((r-l+1) - max(count.values()) > k):
                count[s[l]] -=1
                l+=1
            maxlen = max(maxlen, r - l + 1)

        return maxlen
