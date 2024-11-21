from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
    
ransomNote = "a"
magazine = "ba"

print(Solution().canConstruct(ransomNote, magazine))