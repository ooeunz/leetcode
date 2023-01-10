from typing import List


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


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED") is True)
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE") is True)
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCD") is False)
print(s.exist([["A", "A"]], "AAA") is False)
print(s.exist([["a", "b"]], "ba") is True)
