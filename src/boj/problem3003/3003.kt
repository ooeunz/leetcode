package boj.problem3003

import java.util.Scanner

private val sc = Scanner(System.`in`)
fun main(args: Array<String>) {
    val origins = arrayListOf(1, 1, 2, 2, 2, 8)
    val numbers = sc.nextLine().split(" ").map { it.toInt() }
    val result = origins
        .zip(numbers)
        .map { (origin, number) -> origin - number }
        .joinToString(" ")

    println(result)
}
