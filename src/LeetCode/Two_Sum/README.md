# [Two Sum](https://leetcode.com/problems/two-sum/)

> 2020-10-10

leetcode 입문 문제로 HashMap을 이용하면 간단하게 풀 수 있는 문제입니다. 풀이법은 크게 두가지로 생각해 볼 수 있는데, 앞서 언급한 HashMap을 이용하는 방법과 brute-force로 푸는 방법을 들 수 있습니다.

### solve 1.
먼저 brute-force로 푸는 방법을 살펴보도록 하겠습니다. brute-force는 무식하게 힘으로 푼다라는 뜻을 가진 알고리즘으로 가능한 모든 범위를 탐색하는 알고리즘입니다. 2개의 for문을 중첩으로 두어서 nums[i]와 nums[j]의 합이 target이 될때까지 loop를 돌아서 정답을 찾을 때 return 해주는 방식입니다.

for문이 2번 중첩되어야 하므로 **시간 복잡도**는 `O(n^2)`이지만 상대적으로 **공간 복잡도**는 `O(1)`만큼 필요합니다.
```java
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = 0; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                int[] ret = new int[2];
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }
    }
}
```

### solve 2.
두번째 방법은 HashMap을 이용하는 방법입니다. HashMap은 Hash Collision이 있지 않은 한 O(1)의 시간 복잡도로 데이터를 탐색할 수 있는 자료 구조입니다. 알고리즘은 1번의 for문을 돌게 되고 `target - cur`을 해서 만약 값이 HashMap 안에 없으면 값을 put해주고, 값이 존재하면 해당 값을 return 해주는 방식입니다.

만약 `nums = [2,7,11,15]`, `target = 9`이라면 `i=1` 즉 2가 HashMap에 들어있고 7을 검사할 때 답을 찾게 되기 때문에 결괏 값의 첫번째 값으로 HashMap에 들어있는 값을, 두번 째로 현재 index 값을 넣어 주어야합니다.
한번의 for loop을 돌기 때문에 `O(n)`만큼의 시간 복잡도와 HashMap에 최대 N만큼 데이터를 저장해야하기 때문에 공간 복잡도 역시 `O(n)`입니다.
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        int cur = nums[i];
        if (map.containsKey(target - cur)) {
            int[] ret = new int[2];
            ret[0] = map.get(target - cur);
            ret[1] = i;

            return ret;
        } else {
            map.put(cur, i);
        }
    }
    return null;
}
```