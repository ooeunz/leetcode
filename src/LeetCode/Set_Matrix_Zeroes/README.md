# [Set Matrix Zeroes](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/)

> 2020-12-08

2차원 배열이 주어졌을 때 값이 0인 element를 기준으로 좌우상하를 모두 0으로 바꾸는 문제입니다.
(체스에서 **룩**의 이동할 수 있는 범위라고 생각하면 이해하기 쉽습니다.)

> ##### Follow up
>
> A straight forward solution using O(mn) space is probably a bad idea.
>
> A simple improvement uses O(m + n) space, but still not the best solution.
>
> Could you devise a constant space solution?

# solve 1.
이 문제에서 가장 실수하기 쉬운 부분은 0인 element를 찾았을 때 가로세로를 모두 0으로 변경하고, 
다시 탐색을 시작할 때 이전에 1에서 0으로 변경된 element를 또 다시 기준으로 삼아 가로세로를 0으로 변경하는 오류입니다.

그래서 아래의 풀이에선 가로를 먼저 1에서 0으로 변경하고, 0이 있는 index의 위치를 저장해둡니다.
그리고, 세로를 기준으로 다시한번 반복문을 돌게되고 저장해둔 index의 위치를 기준으로 세로를 0으로 변경합니다.

이와 같은 경우 time complexity는 `O(nm)`만큼 소요되고, 0이었던 index의 위치를 저장해야 하기 때문에 space complexity는 `O(m + n)`이 됩니다.
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = set()
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        col.add(j)
                    else:
                        matrix[i][j] = 0
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0
```