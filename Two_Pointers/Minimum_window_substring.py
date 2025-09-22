"""
Minimum Window Substring

Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "" : return ""

        tdict = {}
        wdict = {}

        for l in t:
            tdict[l] = 1 + tdict.get(l, 0)

        minlen = float("infinity")
        res = [0,0]
        have,need = 0,len(tdict)
        l = 0 

        for r in range(len(s)):
            c = s[r]

            wdict[c] = 1 + wdict.get(c, 0)

            if c in t and wdict[c] == tdict[c]:
                have += 1

            while have == need:

                if (r - l + 1) < minlen:
                    res = [l,r]
                    minlen = r - l + 1

                wdict[s[l]] -= 1
                if s[l] in tdict and wdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1]+1] if minlen < float("infinity") else ""




