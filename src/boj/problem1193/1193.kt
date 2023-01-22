package boj.problem1193

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
