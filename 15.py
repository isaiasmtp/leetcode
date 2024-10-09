from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i] > 0:
                break

            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                three = [nums[i], nums[l], nums[r]]
                sum_three = sum(three)
                if sum_three == 0:
                    ans.append(three)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif sum_three < 0:
                    l+= 1
                else:
                    r -= 1

        return ans