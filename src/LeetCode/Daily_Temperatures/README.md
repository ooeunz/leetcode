# [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

> 2020-12-23

정수로 이루어진 배열이 주어 졌을때 `i`번째 element의 값보다 더 큰 값이 몇번째 뒤에 있는지를 각 index에 저장하여 return 하는 문제입니다.

### solve 1.
주어진 배열을 순환하며 index들을 `stack`에 채워넣습니다. 
그리고 다음 element를 탐색할 때마다 stack의 마지막 값과 비교하여서 만약 값이 크다면 `stack`을 하나씩 pop하면서 값을 비교하고 마지막 index의 값보다 큰 값에서 현재 index를 뺀 값을 `ans` 배열의 `i`번째에 채워넣습니다.
또는 만약 값이 작다면 계속해서 `stack`에 값을 채워넣어줍니다.

`stack`에 값이 계속 채워진다는 것은 현재까지 지나온 값보다 큰 값이 아직 나오지 않았다는 뜻으로 해석할 수 있습니다.
이와같이 for문을 모두 순환한 후에 `ans` 값을 return합니다.

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            if not stack or T[stack[-1]] > T[i]:
                stack.append(i)
            else:
                while stack and T[stack[-1]] < T[i]:
                    j = stack.pop()
                    ans[j] = i - j
                stack.append(i)
        return ans
``` 