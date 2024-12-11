from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevM = {}

        for i in range(len(nums)):
            num = nums[i]
            targetValue = target - num
            if targetValue in prevM:
                return [prevM[targetValue], i]
            else:
                prevM[num] = i

sol = Solution().twoSum([2,7,11,15], 9)
print(sol)