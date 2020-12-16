# [Unique Paths](https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/)

> 2020-12-16

2차원 배열이 주어 졌을 때 왼쪽 가장 위 모서리에서 출발해서 오른쪽 하단의 모서리에 도착 하는데 경로가 몇개 있는 지 return 하는 문제입니다.
이때 이동은 오른쪽과 밑으로만 이동할 수 있습니다.

### solve 1.
해당 문제는 dynamic programing을 이용해서 풀 수 있습니다. 2차원 배열의 각 element의 값은 해당 index까지 올 수 있는 경로의 합입니다.
해당 index까지 올 수 있는 경로의 수는 현재 자신의 index에서 윗칸과 왼쪽 칸의 합이됩니다.

그러기 위해서 먼저 제일 위의 가로 한 줄과 왼쪽의 세로 한 줄을 `1`로 채워줍니다. 왜냐하면 오른쪽 또는 아래로만 이동할 수 있기 때문에
해당 라인은 갈 수 있는 경로가 하나 뿐이기 때문입니다.

그런 다음 하나씩 배열을 돌며 값을 채워 나간 후 마지막 2차원 배열의 마지막 값을 return 합니다.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        matrix = [[1] * n]
        for _ in range(m - 1):
            matrix.append([1] + [0] * (n - 1))

        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
        return matrix[-1][-1]
```