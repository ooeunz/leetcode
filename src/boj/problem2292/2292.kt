package boj.problem2292

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
