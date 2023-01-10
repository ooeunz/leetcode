from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        OCEAN, LAND = "0", "1"
        AROUND = ((0, 1), (0, -1), (1, 0), (-1, 0))
        height, width = len(grid), len(grid[0])

        def in_boundary(r, c):
            return 0 <= r < height and 0 <= c < width

        def find_island(r, c):
            if not in_boundary(r, c) or grid[r][c] == OCEAN:
                return
            grid[r][c] = OCEAN
            for i, j in AROUND:
                nx_y, nx_x = i + r, j + c
                find_island(nx_y, nx_x)

        ans = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == LAND:
                    ans += 1
                    find_island(y, x)
        return ans


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
