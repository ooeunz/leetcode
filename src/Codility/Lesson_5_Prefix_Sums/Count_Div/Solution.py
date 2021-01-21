def solution(A, B, K):
    total = B // K
    d, m = divmod(A, K)
    if m:
        return total - d
    return total - d + 1


print(solution(6, 11, 2))