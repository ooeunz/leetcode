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


s = Solution()
print(s.uniquePaths(3, 7) == 28)
print(s.uniquePaths(3, 2) == 3)

