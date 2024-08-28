from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l

    def removeDuplicatesOld(self, nums: List[int]) -> int:
        l = 0

        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1

nums = [0,0,1,1,1,2,2,3,3,4]

# res = Solution().removeDuplicates(nums)
# print(res)
# print(nums)