/*
MIT License
Copyright 2017 Suhas SG <jargnar@gmail.com>
*/

import scala.util._

object Solution extends App {
    val l = readInt
    val h = readInt
    val t = readLine
    
    val rows = for (_ <- 0 until h) yield readLine
    
    val alphabets = "abcdefghijklmnopqrstuvwxyz"
    val positions = for (letter <- t) yield {
        val pos = alphabets.indexOf(letter.toLower)
        if (pos == -1) 26 else pos
    }
    
    for (row <- rows) {
        for (pos <- positions) {
            for (i <- 0 to l-1) {
                print(row(pos*l + i))    
            }    
        }
        println()
    }
}

