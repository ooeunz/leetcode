# 벌집

벌집의 가장 중심의 `1`을 1단계라고 가정하고 외부로 한칸씩 멀어질때마다 1+n칸 이라고 가정 하겠습니다.

단계가 올라갈수록 구성하고 있는 육각형의 수는 점차 많아지게 되는데 아래와 같이 각 단계를 거듭할 수록 `단계 * 6`을 더한 값이 단계의 마지막 수가 되는 규칙을 찾을 수 있습니다.

```
1단계 - 1번부터 1번까지   (0)
2단계 - 2번부터 7번까지   (6)
3단계 - 8번부터 19번까지  (12)
4단계 - 20번부터 37번까지 (18)
5단계 - 38번부터 61번까지 (24)
```

이러한 규칙을 수식으로 나타내면 아래와 같습니다.

`y 단계의 마지막 수 = x + (y * 6)`

```kotlin
import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)){
    val target = nextLong()
    var end = 1L
    var result = 1L
    while (target > end) {
        end += result * 6
        result++
    }

    println(result)
}

```