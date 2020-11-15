# [Remove Duplicates from Sorted Array](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/)

> 2020-11-15

이 문제는 Space complexity가 O(1)을 맞춰야하는 문제입니다. 따라서 새로운 배열을 할당하거나 `HashTable`을 사용할 수 없습니다.
또 특이하게 return 값만을 확인하는 것이 아니라 정답의 길이만큼 nums 배열의 값을 확인하기 때문에 두가지 정답을 보는 문제입니다.
(이 부분에서 백준 저지의 문제들과 스타일이 달라서 해맸습니다.)


> Clarification:
>
> Confused why the returned value is an integer but your answer is an array?
>
> Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
>
> Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```


### solve 1.
알고리즘은 앞의 for문을 돌면서 이전 loop에서의 값이 현재의 값과 다른지를 확인하여 중복을 검사하는 것입니다.
즉 만약에 중복된 수들이 배열안에 있다면 가장 마지막 중복된 수를 체크할때 `ans += 1`을 해주는 것입니다.
그리고 동시에 nums의 값을 변경해줍니다. (return 외의 정답 값을 위해서)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]
                ans += 1
                index += 1
        return ans + 1
```