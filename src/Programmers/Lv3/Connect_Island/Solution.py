def solution(n: int, costs: list):
    costs.sort(key=lambda x: x[2])
    ans = 0
    visited = {costs[0][0]}

    while n > len(visited):
        for i, val in enumerate(costs):
            start, end, cost = val
            if start in visited and end in visited:
                continue
            if start in visited or end in visited:
                ans += cost
                visited.update([start, end])
                break
    return ans


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4)
