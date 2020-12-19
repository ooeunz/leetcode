# [Word Search](https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/)

> 2020-12-19

Word Search 라는 유명한 게임입니다. 2차원 배열안에 무작위로 알파벳이 주어질 경우, 해당 2차원 배열 안에서 주어진 영단어를 찾는 알고리즘 입니다.
[참고: wikipedia](https://en.wikipedia.org/wiki/Word_search)

다만 해당 문제에선 대각선으로 이어지는 알파벳은 유효하지 않습니다.

### solve 1.
이 문제는 backtracking을 이용해서 풀 수 있습니다. 알고리즘의 핵심 컨셉은 2차원 배열을 하나씩 순환하면서 
- 이때까지 다녀온 길은 다시 가지 않고
- 알파벳을 검사 했을 때 `True`가 아니라면 이전으로 backtracking 하는 것 입니다.

그를 위해 먼저 좌우상하를 검사하기 위한 `ROUND` 변수와, 지금 탐색하는 index가 이전에 들린적이 있는지 확인하기 위한 `used` 2차원 배열을 선언합니다.
다음으로 `board` 또는 `used` 2차원 배열의 값을 넘어가지 않도록 확인하는 `in_boundary` 함수를 선언합니다.

이제 재귀적으로 동작하는 `find_word`함수를 살펴보겠습니다.
먼저 함수의 기저 사례를 살펴보겠습니다. 현재 확인하고 있는 index의 element가 찾고있는 알파벳이 아니라면 `False`를 return 합니다.
만약 우리가 찾고있는 알파벳이 맞다면 현재 찾은 알파벳이 찾고있는 단어의 마지막 알파벳인지 확인합니다. 만약 마지막 알파벳이라면 우리는 원하는 영단어를 `board` 안에서 찾은 것이므로 `True`를 return 해줍니다.

만약 마지막 알파벳이 아니라면, 나머지 알파벳을 찾아야합니다.
주어진 index에서 `ROUND` 튜플 안에 있는 element들을 하나씩 꺼내서 좌우상하로 `find_word`함수를 재귀적으로 실행합니다.
이때 탐색하려는 index는 `board` boundary 안이어야하고, 이때까지 들리지 않은 곳이므로
이전에 선언했던 `in_boundary` 함수와 `used` 배열을 이용합니다.

이와같이 모든 범위의 탐색이 끝나면 `ans`값을 return합니다.

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        ROUND = ((1, 0), (-1, 0), (0, -1), (0, 1))
        used = [[False for _ in range(width)] for _ in range(height)]

        def in_boundary(row, col):
            return 0 <= row < height and 0 <= col < width

        def find_word(row, col, idx, used):
            if board[row][col] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            found = False
            for r, c in ROUND:
                nxt_r, nxt_c = row + r, col + c
                if in_boundary(nxt_r, nxt_c) and not used[nxt_r][nxt_c]:
                    used[nxt_r][nxt_c] = True
                    found = found or find_word(nxt_r, nxt_c, idx + 1, used)
                    used[nxt_r][nxt_c] = False
            return found

        ans = False
        for y in range(height):
            for x in range(width):
                used[y][x] = True
                ans = ans or find_word(y, x, 0, used)
                used[y][x] = False
        return ans
```