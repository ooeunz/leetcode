from typing import List


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
        # This is nothing to do with the answer
        print(matrix)


s = Solution()
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
