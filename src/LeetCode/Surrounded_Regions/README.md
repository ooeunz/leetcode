# [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/submissions/)

> 2020-12-22

`X`와 `O`로 이루어진 2차원 배열이 주어 졌을 때, 4면이 `X`로 둘러싸인 `O`를 `X`로 바꾸는 문제입니다.


### solve 1.
> 처음에는 이 문제를 백트래킹을 이용해서 풀려고 했습니다. `O`를 찾았을 때 `O`의 위치를 keep하고, 재귀적으로 좌우상하를 탐색하여서 
> 4면이 모두 `X`인 경우 `O`를 모두 `X`로 바꿔주었습니다.
> 하지만 구현적으로도 실패하였고, Time Error가 발생하였습니다.

풀이를 보고 문제에 좀 더 유연하게 접근해야 한다는 생각이 든 문제입니다. `O`를 발견했을 때 재귀를 호출해야한다고 생각했지만,
사실 생각해보면 2차원 배열의 테두리에 있는 `O`와 연결된 `O`를 제외한 나머지 `O`는 자연스레 `X`에 둘러쌓인 `X`가 됩니다.

따라서 테두리와 연결된 `O`는 모두 임의로 `1`(`X`에 둘러 쌓이지 않은 `O`라는 표시)로 바꿔준 후, 
다시 한번 2차원 배열을 순환하며 `1`은 `O`로, `O`는 `X`로 변환해줍니다.

총 2차원 배열을 2번 순환해야하므로 `2mn`만큼 for문을 돌게됩니다.
그래서 time complexity는 `O(mn)`이 됩니다.

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        height, width = len(board), len(board[0])
        ROUND = ((0, 1), (0, -1), (-1, 0), (1, 0))
        WHITE, BLACK, LIFE = 'O', 'X', '1'

        def in_boundary(row, col):
            return 0 <= row < height and 0 <= col < width

        def find_LIFE_stone(row: int, col: int):
            if board[row][col] == WHITE:
                board[row][col] = LIFE
            elif board[row][col] == BLACK:
                return

            for r, c in ROUND:
                nxt_r, nxt_c = row + r, col + c
                if in_boundary(nxt_r, nxt_c) and board[nxt_r][nxt_c] == WHITE:
                    find_LIFE_stone(nxt_r, nxt_c)

        for row in range(height):
            find_LIFE_stone(row, 0)
            find_LIFE_stone(row, width - 1)
        for col in range(width):
            find_LIFE_stone(0, col)
            find_LIFE_stone(height - 1, col)
        for row in range(height):
            for col in range(width):
                if board[row][col] == LIFE:
                    board[row][col] = WHITE
                elif board[row][col] == WHITE:
                    board[row][col] = BLACK
```