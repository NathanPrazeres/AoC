package main

import (
	"bufio"
	"fmt"
	"os"
)

func parseInput(path string) ([][]int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}

	defer func() {
		if err := file.Close(); err != nil {
			panic(err)
		}
	}()

	scanner := bufio.NewScanner(file)

	input := [][]int{}

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}

		inputLine := []int{}
		for _, char := range line {
			if char >= '0' && char <= '9' {
				inputLine = append(inputLine, int(char-'0'))
			}
		}

		input = append(input, inputLine)
	}

	return input, nil
}

func intPow(base int, exp int) int {
	result := 1
	for range exp {
		result *= base
	}
	return result
}

func maxJoltage(input [][]int, size int) int {
	result := 0

	for _, bank := range input {
		maxVal := 0
		for i, joltage := range bank {
			for n := min(size-1, len(bank)-i); n > 0; n-- {
				e := intPow(10, n)
				newVal := maxVal/intPow(10, n+1)*e + joltage*e
				if i < len(bank)-n && newVal > maxVal {
					// 9123 -> 4 56 -> 9400
					// maxVal/intPow(10, n+1)*e => 12 -> 00 (n = 1)
					maxVal = newVal
					break

				} else {
					newVal := maxVal/e*e + joltage*intPow(10, n-1)
					if newVal > maxVal {
						maxVal = newVal
						break
					}
				}
			}
		}

		result += maxVal
	}

	return result
}

func main() {
	input, err := parseInput("input.in")
	if err != nil {
		panic(err)
	}

	fmt.Println(maxJoltage(input, 12))
}
