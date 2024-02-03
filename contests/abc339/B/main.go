package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const BUFSIZE = 10000000
var rdr *bufio.Reader

func main() {
	rdr = bufio.NewReaderSize(os.Stdin, BUFSIZE)
	solve()
}

func solve() {
	in1 := mapToIntSlice(input())
	H, W, N := in1[0], in1[1], in1[2]

	grid := make([][]rune, H)
	for i := range grid {
		grid[i] = make([]rune, W)
		for j := range grid[i] {
			grid[i][j] = '.'
		}
	}

	grid[0][0] = '#'
	direction := "right"
	tmp := [2]int{0, 1}

	for i := 0; i < N-1; i++ {
		h, w := tmp[0], tmp[1]
		fmt.Println(h, w, direction)
		switch direction {
		case "right":
			if grid[h][w] == '.' {
				grid[h][w] = '#'
				direction = "down"
				tmp = [2]int{wrapNumber(h + 1, H - 1), w}
			} else {
				fmt.Println("13")
				grid[h][w] = '.'
				direction = "up"
				tmp = [2]int{wrapNumber(h - 1, H - 1), w}
			}
		case "down":
			if grid[h][w] == '.' {
				grid[h][w] = '#'
				direction = "left"
				tmp = [2]int{h, wrapNumber(w - 1, W - 1)}
			} else {
				grid[h][w] = '.'
				direction = "right"
				tmp = [2]int{h, wrapNumber(w + 1, W - 1)}
			}
		case "left":
			if grid[h][w] == '.' {
				grid[h][w] = '#'
				direction = "up"
				tmp = [2]int{wrapNumber(h - 1, H), w}
			} else {
				grid[h][w] = '.'
				direction = "down"
				tmp = [2]int{wrapNumber(h + 1, H), w}
			}
		case "up":
			if grid[h][w] == '.' {
				grid[h][w] = '#'
				direction = "right"
				tmp = [2]int{h, wrapNumber(w + 1, W)}
			} else {
				grid[h][w] = '.'
				direction = "left"
				tmp = [2]int{h, wrapNumber(w - 1, W)}
			}
		}
	}

	for _, row := range grid {
		for _, cell := range row {
			fmt.Print(string(cell))
		}
		fmt.Println()
	}
}

// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// 一行をstringで読み込み
func input() string {
	buf := make([]byte, 0, 16)
	for {
		l, p, e := rdr.ReadLine()
		if e != nil {
			fmt.Println(e.Error())
			panic(e)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}

// string <-> []string
// 第２引数で渡された文字列でsplitする
func strToSlice(input, sep string) []string {
	return strings.Split(input, sep)
}


// // string <-> []int
func mapToIntSlice(input string) []int {
	slice := make([]int, 0)
	lines := strToSlice(input, " ")
	for _, v := range lines {
		// s2iはstringをintに変換する関数(後述)
		slice = append(slice, s2i(v))
	}
	return slice
}

// string <-> int
func s2i(s string) int {
	v, ok := strconv.Atoi(s)
	if ok != nil {
		panic("Faild : " + s + " can't convert to int")
	}
	return v
}

func i2s(i int) string {
	return strconv.Itoa(i)
}

// bool <-> int
func b2i(b bool) int {
	if b {
		return 1
	}
	return 0
}

func i2b(i int) bool {
  return i != 0
}

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func min(values ...int) int {
	ret := values[0]
	for _, v := range values {
		if ret > v {
			ret = v
		}
	}
	return ret
}

func max(values ...int) int {
	ret := values[0]
	for _, v := range values {
		if ret < v {
			ret = v
		}
	}
	return ret
}

func mod(x, y int) int {
	m := x % y
	if m < 0 {
		return m + y
	}
	return m
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func gcd(v1, v2 int) int {
	if v1 > v2 {
		v1, v2 = v2, v1
	}
	for v1 != 0 {
		v1, v2 = v2%v1, v1
	}
	return v2
}

func lcm(v1, v2 int) int {
	return v1 * v2 / gcd(v1, v2)
}

// heap (priority queue)
type intHeap []int
func (h intHeap) Len() int {
	return len(h)
}
func (h intHeap) Less(i, j int) bool {
	return h[i] < h[j]
}
func (h intHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *intHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// wrapNumber は、与えられた数値が0 ~ Nの範囲に収まるように調整する関数です。
func wrapNumber(value int, N int) int {
	// モジュロ演算の結果が負にならないように調整
	if value < 0 {
		return (value%(N+1) + (N + 1)) % (N + 1)
	}
	return value % (N + 1)
}
