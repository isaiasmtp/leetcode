from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_count = [0 for i in range(n+1)]

        for c in citations:
            paper_count[min(n, c)] += 1

        h = n

        papers = paper_count[n]

        while papers < h:
            h-= 1
            papers += paper_count[h]

        return h

nums = [3,0,6,1,5]
res = Solution().hIndex(nums)
print(res)