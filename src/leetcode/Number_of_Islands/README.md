# [Number of Islands](https://leetcode.com/problems/number-of-islands/submissions/)

> 2020-01-03

`1`은 땅이고 `0`은 바다라고 가정 했을 때 몇개의 땅이 있는지를 return 하는 문제입니다.

### solve 1.
먼저 `grid`와 똑같은 크기의 `'0'`으로 이루어진 2차원 배열 `island`를 선언합니다.
이제부터 grid의 index를 하나씩 순환하면서 `grid[y][x]`가 `'1'`이면서 동시에 `island[y][x]`는 `'0'` 이라면 (이거서 `'0'`은 아직 `ans`값에 값을 추가하지 않았다는 뜻입니다.)

`ans += 1`을 해주고, dfs 알고리즘을 이용해서 `grid[y][x]`와 연결된 모든 `'1'`이 있는 영역을 `island`에도 값을 추가해줍니다.
 
모든 for문을 다 돌게된 후 `ans` 값을 return 합니다.
해당 알고리즘의 time complexity는 `O(nm)`입니다.
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        OCEAN, LAND = "0", "1"
        AROUND = ((0, 1), (0, -1), (1, 0), (-1, 0))
        height, width = len(grid), len(grid[0])

        island = [[OCEAN for _ in range(width)] for _ in range(height)]

        def in_boundary(r, c):
            return 0 <= r < height and 0 <= c < width

        def find_island(r, c):
            if not in_boundary(r, c) or grid[r][c] == OCEAN or island[r][c] == LAND:
                return
            island[r][c] = LAND
            for i, j in AROUND:
                nx_y, nx_x = i + r, j + c
                find_island(nx_y, nx_x)

        ans = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == LAND and island[y][x] == OCEAN:
                    ans += 1
                    for dy, dx in AROUND:
                        nxt_y, nxt_x = y + dy, x + dx
                        find_island(nxt_y, nxt_x)
        return ans
```