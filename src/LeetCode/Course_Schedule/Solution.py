from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacency = collections.defaultdict(list)
        for k, v in prerequisites:
            indegree[k] += 1
            adjacency[v].append(k)
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for dest in adjacency[node]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    queue.append(dest)
            adjacency[node] = []
        return len(visited) == numCourses


s = Solution()
print(s.canFinish(2, [[1, 0]]) is True)
print(s.canFinish(2, [[1, 0], [0, 1]]) is False)
print(s.canFinish(3, [[0, 1], [0, 2], [1, 0]]) is False)
print(s.canFinish(2, [[1, 0]]) is True)
print(s.canFinish(2, [[0, 1]]) is True)
print(s.canFinish(2, []) is True)
