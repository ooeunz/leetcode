# [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

> 2020-12-26

정수로 이루어진 배열 `tasks`와 정수 `n`이 주어집니다.
task 배열안의 문자를 하나씩 출력하게 되는데, 이때 동일한 문자가 연속되면 그 사이에 `idle`이 하나 출력 되어야 합니다.
또한 동일한 문자가 연속되지 않더라도 `n`번 `tasks` 안의 문자열이 사용되면 역시 `idle`을 출력 해주어야 합니다.

이러한 조건일 경우 `tasks` 배열 안에 있는 문자들을 조합하여 가장 적은 수만큼 출력할 경우의 수를 return 하는 문제입니다.

### solve 1.
이 문제를 풀기 위해선 문자의 수가 가장 많은 문자들을 먼저 사용하는 것이 핵심 컨셉입니다.

먼저 `tasks` 안에 있는 각각의 문자들을 `collection.Counter` 라이브러리를 이용해서 counter 형태로 만듭니다.
그런 다음 heap 자료구조에 `counter`의 value 값들을 마이너스 형태로 넣어줍니다.

> 여기서 마이너스 형태로 넣어주는 이유는 파이썬의 `heapq` 라이브러리는 최소 힙만을 지원하기 때문에
> 힙에 넣는 값들을 음수로 바꿔줌으로써 최소 힙을 최대 힙처럼 사용할 수 있습니다.

이제 `heap`에 있는 최대 값들을 하나씩 꺼내가며 `heap`이 빌때까지 반복해서 출력합니다.
이때 `n`만큼 출력하면 `idle`이 필수적으로 한번 추가되어야 하므로, 
`n`번 반복하며, 힙에 있는 값을 꺼내고, 만약 값이 `-1`이 아니라면(마지막 값이라면) `+ 1`을 해서 다시 `cycle` 배열에 넣어줍니다.
`cycle` 배열에 넣는 이유는, `n`번만큼 반복 했을 경우, 다시 `idle`을 추가해야 하므로 다시 `heap`에 넣어주기 위해서입니다.

loop 중에 `heap`과 `cycle`이 모두 비게 된다면 모든 값을 출렸했다는 뜻이므로 `ans`를 return 합니다.
`n`번만큼 반복문이 돌았다면 `cycle`에 있는 값을 다시 꺼내서 `heap`에 넣어 다시 최대 값부터 꺼내서 로직을 수행하도록 합니다.

```python
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap, ans = [], 0
        for v in counter.values():
            heapq.heappush(heap, -v)
        while heap:
            idle, cycle = 0, []
            while idle <= n:
                ans += 1
                if heap:
                    v = heapq.heappop(heap)
                    if v != -1:
                        cycle.append(v + 1)
                if not heap and not cycle:
                    return ans
                else:
                    idle += 1
            for v in cycle:
                heapq.heappush(heap, v)
        return ans

```