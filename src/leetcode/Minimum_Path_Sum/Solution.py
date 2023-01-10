from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROUND = ((-1, 0), (0, -1))
        height, width = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(width)] for _ in range(height)]
        dp[0][0] = grid[0][0]

        def in_boundary(row, col):
            return 0 <= row < height and 0 <= col < width

        for row in range(height):
            for col in range(width):
                for r, c in ROUND:
                    past_r, past_c = row + r, col + c
                    if in_boundary(past_r, past_c):
                        dp[row][col] = min(dp[row][col], dp[past_r][past_c] + grid[row][col])
        return dp[-1][-1]


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12)
