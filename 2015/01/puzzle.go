package main

import (
	"fmt"
	"io/ioutil"
)

func getInput() string {
	data, err := ioutil.ReadFile("input")
	if err != nil {
		fmt.Println("error reading input file: ", err)
	}
	return string(data)
}

func puzzle1() {
	fmt.Println("Day 1, puzzle 1 - Not Quite Lisp")
	level := 0
	input := getInput()
	fmt.Printf("length %d\n", len(input))

	for i := 0; i < len(input); i++ {
		if string(input[i]) == "(" {
			level++
		} else if string(input[i]) == ")" {
			level--
		}
	}
	fmt.Printf("Floor: %d\n", level)
}

func puzzle2() {
	fmt.Println("Day 1, puzzle 2 - Not Quite Lisp")
	level := 0
	count := 0
	input := getInput()

	for i := 0; i < len(input); i++ {
		if string(input[i]) == "(" {
			level++
		} else if string(input[i]) == ")" {
			level--
		}
		count++
		if level == -1 {
			break
		}
	}
	fmt.Printf("Level changes: %d\n", count)
}

func main() {
	puzzle1()
	puzzle2()
}
