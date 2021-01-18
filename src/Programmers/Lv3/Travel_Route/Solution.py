from collections import defaultdict


def solution(tickets: list):
    routes = defaultdict(list)
    N = len(tickets)
    for start, end in tickets:
        routes[start].append(end)
    for r in routes:
        routes[r].sort()

    def dfs(cur: str, path: list):
        if len(path) == N + 1:
            return path[:]

        for i, country in enumerate(routes[cur]):
            routes[cur].pop(i)
            path.append(country)
            ret = dfs(country, path)
            if ret:
                return ret
            path.pop()
            routes[cur].insert(i, country)

    ans = dfs("ICN", ["ICN"])
    return ans


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])