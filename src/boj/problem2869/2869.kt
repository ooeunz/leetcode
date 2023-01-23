package boj.problem2869

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
