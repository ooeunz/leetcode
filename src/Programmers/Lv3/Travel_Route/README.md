# [여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)

> 2020-01-18

2차원 배열인 `tickets`이 주어집니다. 각 element들은 `[출발 공항, 도착 공항]` 형태로 이루어져 있습니다.
이때 모든 도시를 다 방문 할 수 있는 루트를 return 하는 문제입니다.

이때 가능한 경로가 2개 이상이라면 알파벳 순서로 가장 앞에 있는 경로를 return 합니다.

### solve 1.
먼저 주어진 배열 tickets을 `{출발 공항: [도착 공항1, 도착공항2 ...], ...}`와 같은 형태로 그래프 `routes`를 만들어줍니다.
그런 다음 가장 알파벳이 빠른 정답을 찾기위해 각 배열들은 정렬해줍니다.

그리고 dfs 알고리즘을 통해 각 경로들이 끝까지 도착할 수 있는지를 확인하게 됩니다.
여기서 주의할 점은 도착 공항이 배열로 이루어져 있끼 때문에, 중복된 도착 공항을 확인하지 않도록, `routes[cur].pop(i)`와 같이 
배열에서 해당 index를 제거하고, 다시 `insert` 해주도록 합니다.

```python
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
```
