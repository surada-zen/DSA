# alternate method using Counter 
# to use dictionary as a key we should sorted on dict.items() and then convert it into tuple


from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            key = Counter(word)            
            res[tuple(sorted(key.items()))].append(word)
        return list(res.values())
