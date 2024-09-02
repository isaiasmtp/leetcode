from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        
        for i in range(target, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0

nums = [2,0,1,0,1]
res = Solution().canJump(nums)
print(res)