# [Plus One](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/)

> 2020-11-28

배열에 있는 수에 1을 더 했을 때 자리 올림(rount up)을 어떻게 구현할 것인가에 관한 문제입니다.

### solve 1.

주어진 digits 배열을 뒤에서 부터 앞으로 loop을 돌게됩니다. 그리고 만약 현재 target으로 잡은 index의 값이 9.
즉 자리 올림이 가능한 경우라면 해당 수를 0으로 만들고 loop를 돌게 됩니다.

loop를 멈추게 되는 경우는, index가 0까지 도착했을 경우, 또는 자리 올림이 이루어지지 않는 경우입니다.
후자의 경우엔 그냥 `digits[i] += 1`을 통해 1을 더해주고, 만약 index가 0까지 갔을 경우엔 해당 값을 0으로 만들고 앞에 `[1]`을 더해주어서 자리 올림을 구현합니다. 
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
            else:
                digits[i] += 1
                break
        return digits
```