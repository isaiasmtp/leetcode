class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split(" ")
        if len(pattern) != len(t):
            return False
        s = pattern

        mapST, mapTS = {}, {}

        for i in range(len(pattern)):
            c1, c2 = s[i], t[i]
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True
    
print(Solution().wordPattern("abba", "dog cat cat dog"))