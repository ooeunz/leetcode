# 1-3.
> 문자열 두 개를 입력으로 받아 그중 하나가 다른 하나의 순열인지 판별하는 메서드를 작성하라.

이와 같은 문제 역시 면접관에게 몇가지 질문을 통해 문제를 구체화하는 것이 중요합니다.
1. 대소문자의 구별이 있는지.
2. 문자열에 공백이 포함되어 있는지.
예를 들어 `dog `와 `god`와 같이 공백의 삽입 여부는 전혀 다른 문자열이 되므로 알고리즘을 풀기 전에 필수적으로 확인하도록 합니다.

### solve 1.
이 문제를 푸는 핵심은 만약 permutation 관계의 두개의 문자열이 존재한다면, 해당 문자열은 서로 같은 문자들이 순서만 바껴있는 것을 이용하는 것입니다.
먼저 두 문자열의 길이가 다르다면 permutation 관계가 아니므로 `false`를 return 합니다.

그런 다음 ASCII 최대 수인 128개의 배열 `letter`을 선언하고, 첫번째 문자열의 각 문자들의 수를 `letter`에 기록합니다.
그 후 비교할 문자열을 순환하며 문자마다 `letter`의 값을 하나씩 빼가는데, 이때 값이 0이하로 떨어지면 문자의 수가 같지 않다는 것으로 판단하고 `false`를 return 합니다.
```java
public class Solution {
    public boolean isPermutation(String str, String compareStr) {
        if (str.length() != compareStr.length()) {
            return false;
        }
        int[] letters = new int[128];

        char[] charArr = str.toCharArray();
        for (char c : charArr) {
            letters[c]++;
        }
        for (int i = 0; i < compareStr.length(); i++) {
            int val = compareStr.charAt(i);
            letters[val]--;
            if (letters[val] < 0) {
                return false;
            }
        }
        return true;
    }
}
```

### solve 2.
비슷한 원리로 두개의 문자열을 정렬하여 문자열 값을 비교하는 방법이 있습니다.
```java
import java.util.Arrays;

public class Solution {
    public String sort(String str) {
        char[] content = str.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }

    public boolean isPermutation(String str, String compareStr) {
        if (str.length() != compareStr.length()) {
            return false;
        }
        return sort(str).equals(sort(compareStr));
    }
}
```