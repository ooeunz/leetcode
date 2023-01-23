# 달팽이는 올라가고 싶다

달팽이는 단 한번 `backword` 값과 관계없이 `forward` 값만큼 이동할 수 있다는 점입니다.
그러므로 `goal - forward`를 한 값에서 매일 이동할 수 있는 값 `val step = forward - backward`의 몫(이동한 날 수)와 나머지가 존재한다면 +1을 하여서
총 `forward만 간 1` + `step으로 이동한 수 n` + `나머지가 있는 경우 1`의 총합이 정답이 됩니다.

해당 문제는 수행시간이 극히 짧은 문제입니다. 때문에 최초 `Scanner`를 이용하여 문제를 풀었을 때 시간 초과가 발생했고, BufferReader로 변경 후 제출하여 통과하였습니다.
Time limit이 짧은 문제의 경우 BufferReader를 이용하여 Input을 받는 것이 좋을 것 같습니다.

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (forward, backward, goal) = br.readLine().split(" ").map { it.toLong() }
    goal -= forward

    if (goal <= 0) {
        println(1)

    } else {
        var result = 1L
        val step = forward - backward

        result += goal / step
        val remain = goal % step
        if (remain > 0) {
            result++
        }

        println(result)
    }
    br.close()
}

```