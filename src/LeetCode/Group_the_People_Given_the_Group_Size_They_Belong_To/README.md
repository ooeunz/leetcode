# [Group the People Given the group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/)

> 2020-01-03

정수로 이루어진 배열이 있을 경우, 배열의 각 값들은 해당 index가 몇개의 index가 모일 수 있는 group에 속하는지를 나타냅니다.
`groupSizes`안에 있는 각 index들이 value가 같은 것들끼리 그룹핑하여 return 합니다.

### solve 1.
default value를 list로 갖는 dictionary를 선언합니다.
그리고 `groupSizes`를 하나씩 순환하면서 `{groupSizes[i]: [i]}`의 형태로 `groupSizes[i]`를 key로 갖고 같은 그룹에 속하는 index를 배열로 갖도록 합니다.
이때 만약 배열의 길이가 key와 같다면 해당 값을 `ans`에 copy합니다.

문제에 정답이 없는 경우는 없다고 하였으므로 for문이 끝나면 모든 `groupSize`의 index들이 그룹핑되었다는 것을 알 수 있습니다.
for문이 끝났다면 `ans` 값을 return해줍니다.

해당 문제의 time complexity는 groupSizes만큼 반복문을 순환하기 때문에 `O(n)`입니다.
```python
import collections


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        pkg = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            pkg[groupSizes[i]].append(i)
            if len(pkg[groupSizes[i]]) == groupSizes[i]:
                ans.append(pkg[groupSizes[i]][:])
                pkg[groupSizes[i]] = []
        return ans
```