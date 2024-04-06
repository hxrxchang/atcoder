package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type BingoVal [][]int
type Bingo [][]bool

func numbers(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, _ := strconv.Atoi(f)
		n = append(n, i)
	}
	return n
}

func main() {
	var bingoVal BingoVal
	var bingo Bingo
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < 3; i++ {
		scanner.Scan()
		lowVal := numbers(scanner.Text())
		bingoVal = append(bingoVal, lowVal)
		bingo = append(bingo, []bool {false, false, false})
	}

	scanner.Scan()
	times, _ := strconv.Atoi(scanner.Text())
	for i := 0; i < times; i++ {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		for i := 0; i < len(bingoVal); i++ {
			for j := 0; j < len(bingoVal); j++ {
				if bingoVal[i][j] == v {
					bingo[i][j] = true
				}
			}
		}
	}

	result := "No"

	for i := 0; i < len(bingo); i++ {
		if bingo[i][0] && bingo[i][1] && bingo[i][2] {
			result = "Yes"
		} else if bingo[0][i] && bingo[1][i] && bingo[2][i] {
			result = "Yes"
		}
	}

	if bingo[0][0] && bingo[1][1] && bingo[2][2] {
		result = "Yes"
	}

	if bingo[0][2] && bingo[1][1] && bingo[2][0] {
		result = "Yes"
	}

	fmt.Println(result)
}
