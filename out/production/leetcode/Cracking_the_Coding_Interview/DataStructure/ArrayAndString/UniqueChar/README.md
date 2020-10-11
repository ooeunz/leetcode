# ArrayAndString

### 1-1. 
> Q. 문자열에 포함된 문자들이 전부 유일한지를 검사하는 알고리즘을 구현하라. 다른 자료구조를 사용할 수 없는 상황이라면 어떻게 하겠는가?

해당 문제를 풀이하기 전에 가장 먼저 확인 해야할 점은 문자열이 ASCII Code인지 UNICODE를 확인하는 것입니다. 이에 따라 탐색해야 하는 범위의 차이가 있기 때문이다. (탐색 범위의 차이가 있을 뿐 알고리즘 자체는 차이가 없습니다.)

문자열이 ASCII 코드라고 가정 할 경우 이 문제를 가장 쉽게 풀 수 있는 방법은 for문을 2개 중첩하여 배열 안에 있는 모든 수를 비교하는 것입니다. 그렇게 되면 시간 복잡도는 `O(n^2)`가 될 것입니다.

다른 방법은 배열을 이용하여 푸는 방법입니다. ASCII Code가 모두 256개이므로 256개로 이루어진 배열을 생선한 이후, ASCII Code가 배열의 index 값에 채워져 있는지를 확인하므로 문제를 해결할 수 있습니다. 그렇게 되면 시간복잡도는 `O(n)` 공간 복잡도는 `O(n)`(문자열의 길이)으로 문제를 풀 수 있습니다.
```java
public boolean isUniqueChars2(String str) {
    if (str.length() > 256) {
        return false;
    }
    boolean[] charSet = new boolean[256];
    for (int i = 0; i < str.length(); i++) {
        int val = str.charAt(i);
        if (charSet[val]) {
            return false;
        }
        charSet[val] = true;
    }
    return true;
}
``` 
하지만 이 보다 공간을 절약할 수 있는 방법이 있습니다. 바로 배열 대신 **비트 벡터**를 이용하는 방법입니다.
이번 예시에서는 편의를 위해 ASCII Code 전체가 아닌 소문자 26자만을 이용하여 풀이를 작성하였습니다.

```java
public boolean isUniqueChar(String str) {
    if (str.length() > 26) {
        return false;
    }
    int checker = 0;
    for (int i = 0; i < str.length(); i++) {
        int val = str.charAt(i) - 'a';
        if ((checker & (1 << val)) > 0) {
            return false;
        }
        checker |= (1 << val);
    }
    return true;
}
```
해당 풀이는 비트 연산에서 and 연산시 0과 1이 만나면 0이 return되고 1과 1 또는 0과 0이 만나면 1이 return 되는 것을 이용합니다.
str 문자열에서 문자를 하나씩 꺼내서 'a' char와 빼서 0부터 25까지의 숫자를 추출해주고, 해당 수만큼 1에서 left shift를 하게 됩니다.

그 후 checker에서 & 연산을 이용해서 이전에 있었던 수라면 return false를, 이전에 없었던 수라면  | 연산을 이용해서 checker 변수에 해당 비트를 추가해줍니다.
이와 같이 풀이하면 배열이 아니라 int 변수 하나만을 이용해서 문제를 풀이할 수 있습니다.

### 1-3
> 문자열 두 개를 입력으로 받아 그중 하나가 다른 하나의 순열인지 팔별하는 메서드를 작성하라.
