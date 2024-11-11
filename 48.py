from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l, r, t, b = 0, n, 0, n

        while l < (r-1):
            for i in range(r - l - 1):
                to_right = matrix[l][l + i]

                to_bottom = matrix[t + i][r-1]
                to_left = matrix[b-1][r-i-1]
                to_top = matrix[b-i-1][t]

                matrix[t + i][r-1] = to_right
                matrix[b-1][r-i-1] = to_bottom
                matrix[b-i-1][t] = to_left
                matrix[l][l + i] = to_top
            l += 1
            r -= 1
            t += 1
            b -= 1


matrix =  [[5,1,9,11],
           [2,4,8,10],
           [13,3,6,7],
           [15,14,12,16]]

Solution().rotate(matrix)