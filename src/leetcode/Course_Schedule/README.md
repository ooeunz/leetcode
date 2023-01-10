# [Course Schedule](https://leetcode.com/problems/course-schedule/submissions/)

> 2020-01-14

`0`부터 `numCourses - 1`까지의 수업이 존재합니다. 
존재하는 수업 중 몇몇은 선수과목이 필요한데 `[1, 0]`와 같은 형태로 선수과목에 대한 정보를 나타냅니다. 이와 같은 경우 `1`수업을 듣기 위해선 `0` 수업을 먼저 수강해야한다는 뜻입니다.
선수과목은 `prerequisites` 2차원 배열로 나타내집니다.

### solve 1.
이 문제는 대표적인 그래프 **위상정렬** 문제입니다. 
그래프에서 어떤 node로 오기위한 edge의 수를 in degree라고 하고, 그 node에서다른 node로 향하는 edge를 out degree라고 부릅니다.

알고리즘의 핵심은 
1. `in_degree`가 `0`인 node들을 `queue`에 넣어주고 해당 node 에 연결된 `out_degree`를 모두 삭제해 줍니다.
2. `out_degree`의 삭제로 인해 `in_degree`가 `0`이 된 node들을 `queue`에 넣어줍니다.
3. 1번과 2번을 반복합니다.
4. 방문한 node들의 길이 `visited`와 `numCourses`의 길이를 비교하여, 길이가 같다면 `True` 아니라면 `False`를 return 합니다.

```python
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adjacency = collections.defaultdict(list)
        for k, v in prerequisites:
            in_degree[k] += 1
            adjacency[v].append(k)
        queue = collections.deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for out_degree in adjacency[node]:
                in_degree[out_degree] -= 1
                if in_degree[out_degree] == 0:
                    queue.append(out_degree)
            adjacency[node] = []
        return len(visited) == numCourses
```