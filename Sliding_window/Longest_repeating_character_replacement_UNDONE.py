class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        maxlen = 0
        lp = 0
        rp = 0
        tolerance = 0
        
        while rp < size:
            length = rp - lp + 1
            if s[lp] == s[rp]:
                maxlen = max(length,maxlen)
            elif s[lp] != s[rp] and tolerance < k:
                tolerance += 1
                maxlen = max(length,maxlen)
            else:
                while s[lp] == s[lp+1]:
                    lp+=1  
                lp+=1              
                tolerance = 0
                rp = lp
            rp+=1
        return maxlen
