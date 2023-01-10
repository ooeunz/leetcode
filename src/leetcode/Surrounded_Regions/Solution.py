from typing import List


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

        # This is nothing to do with the answer
        print(board)


s = Solution()
print(s.solve([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]))
print(s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
print(s.solve([["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]))
print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
