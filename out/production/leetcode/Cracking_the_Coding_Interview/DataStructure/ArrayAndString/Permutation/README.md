# 1-3.
> 문자열 두 개를 입력으로 받아 그중 하나가 다른 하나의 순열인지 판별하는 메서드를 작성하라.

이와 같은 문제 역시 면접관에게 몇가지 질문을 통해 문제를 구체화하는 것이 중요합니다.
1. 대소문자의 구별이 있는지.
2. 문자열에 공백이 포함되어 있는지.
예를 들어 `dog `와 `god`와 같이 공백의 삽입 여부는 전혀 다른 문자열이 되므로 알고리즘을 풀기 전에 필수적으로 확인하도록 합니다.

### solve 1.
가장 간단하게 생각 해볼 수 있는 방법은 첫번째 문자열의 모든 순열을 구한 다음 두번째 문자열이 그 순열에 포함되는지 확인하는 방법일 것입니다. (예전의 나라면 이렇게 문제를 풀었을 것 같다.😂)
하지만 순열의 정의를 생각해보면 간단하게 동일한 요소가 들어있는 문자열의 순서만 다른 것입니다. 즉, 간단하게 두 문자열을 정렬하여 값이 같은지만으로 정답을 구할 수 있습니다.
```java
private String sort(String str) {
    char[] contents = str.toCharArray();
    Arrays.sort(contents);
    return new String(contents);
}

public boolean isPermutation(String str, String compareStr) {
    String sortedStr = sort(str);
    String sortedCompareStr = sort(compareStr);

    return sortedStr.equals(sortedCompareStr);
}
```

### solve 2.
위의 풀이법도 좋은 풀이법이지만 만약 효율성이 극도로 필요한 상황이라면 아래와 같은 방법으로 알고리즘을 풀이할 수 있습니다. 위의 풀이가 순열이 같은 문자들이 순서만 바뀐 것을 이용한 것이라면 **문자의 출현 횟수도 동일** 하다는 것을 이용한 풀이법입니다.
첫번째 배열의 문자의 출현 횟수를 기록한 다음 두번째 배열의 출현 횟수와 비교하는 방식으로 문제를 풀 수 있습니다.
```java
public boolean isPermutation2(String str, String compareStr) {
    if (str.length() != compareStr.length()) {
        return false;
    }

    int[] letters = new int[256];
    char[] charArray = str.toCharArray();
    for (char c : charArray) {
        letters[c]++;
    }

    for (int i = 0; i < compareStr.length(); i++) {
        int val = compareStr.charAt(i);
        if (--letters[val] < 0) {
            return false;
        }
    }
    return true;
}
```