from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        r = l = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps+=1
        return jumps

    
        

nums = [2,3,5,9,0,9,7,2,7,9,1,7,4,6,2,1,0,0,1,4,9,0,6,3]
res = Solution().jump(nums)
print(res)