# 손익분기점

가변비용에서 제품의 가격을 제외하면 순수익을 구할 수 있습니다.

이때 `고정비용 / 순수익`을 나누어서 적자의 마지막 시점을 구한 후 `+1`을 하여서 첫 수익이 발생하기 시작하는 손익 분기점을 구합니다.
```kotlin
import java.util.Scanner

private val sc = Scanner(System.`in`)

fun main(args: Array<String>) {
    val (fixedCoset, variabilityCost, price) = sc.nextLine().split(" ").map { it.toLong() }
    val profit = price - variabilityCost
    if (profit <= 0) {
        println(-1)
    } else {
        println(fixedCoset / profit + 1)
    }
}

```