package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readFile(path string) ([]int, error) {
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

	input := []int{}

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		switch line[0] {
		case 'R':
			number, err := strconv.Atoi(strings.Split(line, "R")[1])
			if err != nil {
				return nil, err
			}

			input = append(input, number)
		case 'L':
			number, err := strconv.Atoi(strings.Split(line, "L")[1])
			if err != nil {
				return nil, err
			}

			input = append(input, 0-number)
		}
	}

	return input, nil
}

func doorCode(input []int, clickMethod bool) int {
	dial := 50
	count := 0

	for _, n := range input {
		dial += n
		if clickMethod {
			passes := dial / 100
			if passes < 0 {
				passes = 0 - passes
			}
			if dial < 0 && dial != n {
				passes += 1
			}

			if dial%100 == 0 && passes != 0 {
				passes -= 1
			}

			count += passes
		}

		dial %= 100
		if dial < 0 {
			dial += 100
		}
		if dial == 0 {
			count += 1
		}
	}

	return count
}

func main() {
	input, err := readFile("input.in")
	if err != nil {
		panic(err)
	}

	fmt.Println(doorCode(input, false))
	fmt.Println(doorCode(input, true))
}
