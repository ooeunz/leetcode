# [Queries on a Permutation With Key](https://leetcode.com/problems/queries-on-a-permutation-with-key/)

> 2020-01-15

`1`부터 `queries.length - 1` 만큼의 수들이 있을 때, `queries`안에 있는 수들을 하나씩 찾아서 제일 앞으로 옮기는 문제입니다.

### solve 1.
문제에 주어진 그대로 코드를 짜면 됩니다. 먼저 `1`부터 `queries.length - 1`까지 수 조합을 만들고,
`queries`에서 수를 하나씩 꺼내서, 제일 앞으로 값을 옮겨줍니다.

그 과정에서 `query`의 위치를 `ans` 배열에 담아줍니다.
```python
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        ans = []
        for query in queries:
            pos = p.index(query)
            ans.append(pos)
            p = [p[pos]] + p[:pos] + p[pos + 1:]
        return ans
```