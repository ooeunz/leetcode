# [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)

> 2020-01-22

### solve 1.
이 문제는 크루스칼 알고리즘을 이용해서 풀 수 있는 문제입니다. 
크루스칼 알고리즘이란 **탐욕적인 방법(greedy method) 을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것**입니다.

```python
def solution(n: int, costs: list):
    # 1.
    costs.sort(key=lambda x: x[2])
    ans = 0
    # 2.
    visited = {costs[0][0]}

    while n > len(visited):
        for i, val in enumerate(costs):
            start, end, cost = val
            # 3.
            if start in visited and end in visited:
                continue
            # 4.
            if start in visited or end in visited:
                ans += cost
                visited.update([start, end])
                break
    # 5.
    return ans
```

1. 최소 비용으로 주어진 노드들을 연결하기 위해 비용을 기준으로 배열을 정렬합니다.
2. 중복된 node를 방문하지 않도록 방문한 node를 기록합니다.
3. 두개의 노드가 모두 방문하지 않았다면, 아직 해당 노드까지 최소 비용으로 연결되지 않았다는 것을 뜻하기 때문에 continue 합니다.
4. 만약 두개의 노드 중 하나를 방문했다면, 현재 노드까지의 `cost`를 더해주고 반복문을 `break` 합니다. 
이때 반복문을 더 수행하지 않고, `break`하는 이유는 현재 탐색중인 index 이전에 최소 비용으로 연결할 수 있는 노드가 존재할 수 있기 때문입니다.
5. 반복문 while은 `visited`의 길이가 `n`과 같아질 경우. 
즉 모든 노드가 이어졌을 경우 탈출합니다. 만약 이 이후로 반복문이 계속 이어진다면, 최소의 비용으로 이어진 간선 이외로 모든 간선들이 연결될 것 입니다.
