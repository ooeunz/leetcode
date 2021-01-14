from typing import List
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


s = Solution()
print(s.canFinish(2, [[1, 0]]) is True)
print(s.canFinish(2, [[1, 0], [0, 1]]) is False)
print(s.canFinish(3, [[0, 1], [0, 2], [1, 0]]) is False)
print(s.canFinish(2, [[1, 0]]) is True)
print(s.canFinish(2, [[0, 1]]) is True)
print(s.canFinish(2, []) is True)
