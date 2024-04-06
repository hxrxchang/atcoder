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
	input()
	A := strToIntSlice(input())
	B := strToIntSlice(input())
	C := strToIntSlice(input())

	A2 := map[int]int{}
	B2 := map[int]int{}
	C2 := map[int]int{}

	for _, a := range(A) {
		A2[a%46]++
	}
	for _, b := range(B) {
		B2[b%46]++
	}
	for _, c := range(C) {
		C2[c%46]++
	}

	cnt := 0
	for i := 0; i < 46; i++ {
		for j := 0; j < 46; j++ {
			for k := 0; k < 46; k++ {
				if (i + j + k) % 46 == 0 {
					cnt += A2[i] * B2[j] * C2[k]
				}
			}
		}
	}
	fmt.Println(cnt)
}

// ------------------------------------------------------------------------------------------------------------------------------------------------
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

func strToSlice(input string) []string {
	return strings.Split(input, " ")
}

func strToIntSlice(input string) []int {
	slice := make([]int, 0)
	lines := strToSlice(input)
	for _, v := range lines {
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
