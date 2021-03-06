# 1-1. 중복이 없는가

> 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라.
>
> 자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.

### solve 1.
문제는 파라미터로 받는 String 값이 ASCII 문자열인지, 유니코드 문자열인지에 따라 풀이 방법이 달라지게 됩니다.
만약 ASCII 문자열이라면, ASCII는 0부터 127까지 이루어져 있으므로 128 이상의 길이의 문자열이 파라미터로 들어온다면 바로 `false`를 return 할 수 있습니다.

그런 다음 128 길이의 `boolean` 배열을 선언한 후에, 각 문자열의 문자 ASCII 값을 index로 하는 배열의 값을 `true`로 변경해줍니다.
이러한 로직을 반복하며 만약 이미 `true`로 변경된 문자가 있다면 중복이 있다는 뜻이므로 `false`를 return 합니다.

이 코드의 time complexity는 전체 문자열을 한번씩 확인하게 되므로 `O(N)`이며, space complexity는 `charSet` 배열의 길이가 항상 상수 값이므로 `O(1)` 입니다. 
```java
public class Solution {
    public boolean isUniqueChars(String s) {
        if (s.length() > 127) {
            return false;
        }
        boolean[] charSet = new boolean[128];
        for (int i = 0; i < s.length(); i++) {
            int asciiCode = s.charAt(i);
            if (charSet[asciiCode]) {
                return false;
            }
            charSet[asciiCode] = true;
        }
        return true;
    }
}
```

### solve 2.
문자열이 a ~ z로만 이루어져있다고 가정한다면 비트 연산을 이용해서 문제를 풀 수도 있습니다.

```java
public class Solution {
    public boolean bitSolution(String s) {
        int check = 0;
        for (int i = 0; i < s.length(); i++) {
            int val = s.charAt(i) - 'a';
            if ((check & (1 << val)) > 0) {
                return false;
            }
            check |= (1 << val);
        }
        return true;
    }
}

```

### solve 3.
때로는 문제의 요구사항에 따라, 문자열을 정렬한 후 문자열을 순회하며 인접한 문자의 값들을 비교하여 풀이할 수 있습니다.
하지만 이러한 경우 정렬 알고리즘에 따라 추가적인 공간을 사용한다는 것을 염두해야 합니다.