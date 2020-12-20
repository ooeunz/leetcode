# [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/submissions/)

> 2020-12-20

정수로 이루어진 2차원 배열이 주어 졌을 때, 왼쪽 위 모서리에서 오른쪽 밑 모서리까지 도달해가며 들린 index의 value들의 합이 가장 작도록 하는 문제입니다.

### solve 1.
이 문제는 dynamic programing을 이용해서 풀 수 있습니다. 주어진 `grid` 배열과 동일한 크기의 `dp` 배열을 선언합니다.
배열의 각각의 index는 **현재까지 들린 경로의 합이 가장 작은 경우**를 나타냅니다. 2중 for문을 이용해서 grid 배열을 순환하며,
현재 탐색하고 있는 `grid`의 값 `grid[row][col]`와 위의 index 또는 왼쪽의 index(이전에 들렸던 경로의 최적해) `dp[past_r][past_c]` 중 값이 작은 값(최적해)을 `dp[row][col]`에 저장합니다.

이와 같이 for문을 모두 돌게되면 제일 마지막 `dp` 배열의 마지막 값을 return 합니다.
해당 알고리즘의 time complexity는 `grid` 배열의 전체를 순환해야하므로 `O(nm)`이고, 
같은 맥락으로 `grid`배열과 크기가 같은 `dp`배열을 선언해야하므로 space complexity 역시 `O(nm)`입니다.

```python
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
``` 