def solution(S):
    OPEN, CLOSE = '(', ')'
    stack = []
    for s in S:
        if s == OPEN:
            stack.append(OPEN)
        elif s == CLOSE:
            if not stack:
                return 0
            stack.pop()
    return 0 if stack else 1


print(solution("(()(())())") == 1)
print(solution("())") == 0)
