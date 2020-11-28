# [Move Zeroes](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/)

> 2020-11-28

모든 0을 배열의 끝으로 이동시키고, 동시에 0을 제외한 다른 수는 배열 앞으로 밀착시키는 문제입니다.

또한, 추가적인 배열을 메모리에 할당하지 않고, 최소한의 time complexity만으로 문제를 해결하도록 조건이 주어집니다.

### solve 1.
이 문제를 핵심적인 방법은 0의 수를 기록하는 `cnt`변수와, 배열 앞에서부터 0 아닌 수를 차례대로 채워넣기 위한 위치를 가리키는 `pos` 변수를 이용하는 것입니다.

만약 0을 만나게 될 경우 `cnt += 1`을 해주고 해당 0의 위치에 다른 값을 채워 넣어야하므로 `pos`는 값을 변경시키지 않습니다.

이제 0이 아닌 경우의 수를 만난다면 `pos`의 자리에 해당 값을 채우게 됩니다. 이때 이전에 0이 존재했었다면 자리가 변경되지만, 이전에 0이 없었다면 자신의 자리에 그대로 있게 됩니다.
loop를 모두 순회한 후엔 `cnt`의 수만큼 뒤에서부터 앞으로 0으로 채워주게 됩니다.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        pos = 0
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                nums[pos] = num
                pos += 1
        while cnt > 0:
            nums[len(nums) - cnt] = 0
            cnt -= 1
``` 