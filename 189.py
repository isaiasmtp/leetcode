from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        l, r = 0, len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -=  1

        l, r = 0, k - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -=  1

        l, r = k, len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -=  1

nums = [1,2,3,4,5]
Solution().rotate(nums, 2)

print(nums)