def solution(X, Y, D):
    reach = Y - X
    d, m = divmod(reach, D)
    if m:
        return d + 1
    return d


print(solution(10, 85, 30) == 3)
print(solution(10, 100, 10) == 9)
