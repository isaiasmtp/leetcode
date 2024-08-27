from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# nums = [3,2,2,3]
# val = 2

# res = Solution().removeElement(nums, val)
# print(res)
# print(nums)