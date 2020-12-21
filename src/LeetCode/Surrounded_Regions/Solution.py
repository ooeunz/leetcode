from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        height, width = len(board), len(board[0])
        ROUND = ((0, 1), (0, -1), (-1, 0), (1, 0))
        WHITE, BLACK = 'O', 'X'

        black = [[board[i][j] for i in range(height)] for j in range(width)]

        def in_boundary(row, col):
            return 0 <= row < height and 0 <= col < width

        def convert(row: int, col: int, black: list):
            if board[row][col] == BLACK:
                return True

            white_box.append((row, col))
            dead = True
            for r, c in ROUND:
                nxt_r, nxt_c = row + r, col + c
                if not in_boundary(nxt_r, nxt_c):
                    return False
                if black[nxt_r][nxt_c] != BLACK:
                    black[row][col] = BLACK
                    dead = dead and convert(nxt_r, nxt_c, black)
                    black[row][col] = WHITE
            return dead

        for row in range(height):
            for col in range(width):
                white_box = []
                if board[row][col] == WHITE and convert(row, col, black):
                    while white_box:
                        r, c = white_box.pop()
                        board[r][c] = BLACK

        print(board)


s = Solution()
print(s.solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]))
print(s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
