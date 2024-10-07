from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        sum = numbers[r] + numbers[l] 

        while sum != target:
            if sum > target:
                r -= 1
            else:
                l += 1
            sum = numbers[r] + numbers[l]

        return [l+1, r+1]
        

numbers = [2,7,11,15]
target = 18

res = Solution().twoSum(numbers, target)
print(res)