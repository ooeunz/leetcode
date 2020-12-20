# [Combination Sum](https://leetcode.com/problems/combination-sum/)

> 2020-12-19

정수로 이루어진 배열이 주어졌을 때, 배열안에 주어진 정수를 이용해서 `target`을 만들 수 있는 조합을 모두 만들어서 return하는 문제입니다.

### solve 1.
기본적인 알고리즘 컨셉은 `target`이 `0`이 될때까지 recursion을 호출하며 조합을 만드는 것입니다.
재귀적으로 `target`의 값을 줄여가며 만약 `target`이 `0`이 되면 조합을 찾은 것이므로 `ans`에 값을 추가합니다.
또한 만약 `target`이 0보다 값이 적다면 return 해줍니다.

이제 남은 경우는 아직 `target`이 `0`보다 값이 큰 것이므로 `0`이 되도 배열안에 있는 element를 이용해서 또 다른 recursion을 호출하는 것입니다.
이전에 사용했던 cadidate는 사용하지 않기 위해 `start` 값을 구하게 되는데, 이때 바로 이전에 사용했던 수는 재차 사용할 수 있도록, (즉 8을 만들기 위해 2가 4개 필요한 것처럼)
`chosen` 마지막에 있는 element부터 for문을 돌도록 합니다.

모든 재귀호출이 끝나면 `ans`값을 return합니다.

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def generate(chosen: list, target: int):
            if target == 0:
                chk = sorted(chosen[:])
                if chk not in ans:
                    ans.append(chk)
            if target < 0:
                return

            start = candidates.index(chosen[-1]) if chosen else 0
            for i in range(start, len(candidates)):
                chosen.append(candidates[i])
                generate(chosen, target - candidates[i])
                chosen.pop()
        generate([], target)
        return ans
```