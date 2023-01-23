# [분수찾기](https://www.acmicpc.net/problem/1193)

왼쪽 최상단을 기준으로 x번째 row에 존재하는 row의 경우 대각선에 존재하는 분수의 수는 x개가 됩니다.
예를 들면 3번째 row의 대각선은 총 3개의 분수(`1/3`, `2/2`, `3/1`)로 이루어져 있습니다.

또한 x번째 row가 짝수인 경우 grid의 위에서 좌측 하단 방향으로 수를 전개하며, 홀 수인 경우 그 반대입니다.

그러므로 console로 입력 받은 값 `target`이 누적된 grid size보다 클때까지 grid의 row을 점차 확장 시켜줍니다.
그리고 해당 칸의 대각선의 몇번째에 존재하는 값인지를 구한 뒤(`step`), row가 짝수인지 혹은 홀수인지 확인한 후 `(분자++, 분모--)`과 `(분자--, 분모++)` 값을 계산하여 print 합니다. 

```kotlin
import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val target = nextLong()

    var gridSize = 1
    var row = 1
    while (target > gridSize) {
        gridSize += ++row
    }

    val step = target - (gridSize - row)
    val result = if (row % 2 == 0) {
        val move = step - 1
        "$step/${row - move}"
    } else {
        val move = step - 1
        "${row - move}/$step"
    }
    println(result)
}

```