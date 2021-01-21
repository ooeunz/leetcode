def solution(N):
    binary = str(bin(N))
    mx = 0
    l, find = 0, False
    for i in range(2, len(binary)):
        if not find and binary[i] == "1":
            find = True
        elif find and binary[i] == "0":
            l += 1
        elif find and binary[i] == "1":
            mx = max(l, mx)
            l = 0
    return mx


print(solution(9) == 2)
print(solution(529) == 4)
print(solution(20) == 1)
print(solution(15) == 0)
print(solution(32) == 0)


