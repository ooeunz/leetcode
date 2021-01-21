def solution(A):
    nums = set(A)
    for i in range(1, 1000001):
        if i not in nums:
            return i


print(solution([1, 3, 6, 4, 1, 2]) == 5)
print(solution([1, 2, 3]) == 4)
print(solution([-1, -3]) == 1)
