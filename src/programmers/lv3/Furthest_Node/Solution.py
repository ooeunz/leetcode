from collections import defaultdict, deque


def solution(n: int, edge: list):
    graph = defaultdict(list)
    for k, v in edge:
        graph[k].append(v)
        graph[v].append(k)

    visited = {}
    mx = 1
    queue = deque([(1, 1)])
    while queue:
        node, distance = queue.popleft()
        if node not in visited:
            visited[node] = distance
            mx = max(mx, distance)
        while graph[node]:
            pop = graph[node].pop()
            if pop not in visited:
                queue.append((pop, distance + 1))
    return len(list(filter(lambda x: visited[x] == mx, visited)))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))