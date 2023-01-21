package boj.problem1712

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
