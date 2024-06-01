package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math/big"
	"os"
	"sort"
	"strconv"
	"strings"

	"github.com/liyue201/gostl/ds/set"
	"github.com/liyue201/gostl/utils/comparator"
	"golang.org/x/exp/constraints"
)

const BUFSIZE = 10000000
const MOD = 1000000007
const BIGGEST = int(1e18)
var rdr *bufio.Reader

func main() {
	rdr = bufio.NewReaderSize(os.Stdin, BUFSIZE)
	solve()
}

type Input struct {
	size int
	values []int
	result string
}

func solve() {
	in := getInts()
	n, m, k := in[0], in[1], in[2]
	keys := make([]int, n)
	for i := 0; i < n; i++ {
		keys[i] = i + 1
	}
	combinationsCh := getCombinations(keys, k)
	combinations := make([][]int, 0)
	for comb := range combinationsCh {
		combinations = append(combinations, comb)
	}

	inputs := make([]Input, m)
	for i := 0; i < m; i++ {
		in := getStrs()
		c := s2i(in[0])
		r := in[len(in)-1]
		tmpkeys := make([]int, c)
		for j := 0; j < c; j++ {
			tmpkeys[j] = s2i(in[j+1])
		}
		inputs[i] = Input{size: c, values: tmpkeys, result: r}
	}

	cnt := 0
	for _, comb := range combinations {
		flag := true
		for _, input := range inputs {
			flag2 := true
			fmt.Println(comb, input.values, input.result)
			// if input.result == "x" {
			// 	for _, key := range comb {
			// 		if sliceContains(input.values, key) {
			// 			flag2 = false
			// 			break
			// 		}
			// 	}
			// } else {
			// 	for _, key := range comb {
			// 		if !sliceContains(input.values, key) {
			// 			flag2 = false
			// 			break
			// 		}
			// 	}
			// }
			flag = flag2
		}
		if flag {
			cnt++
		}
	}

	fmt.Println(cnt)
}

// func solve() {
// 	in := getInts()
// 	// n, m, k := in[0], in[1], in[2]
// 	m, k := in[1], in[2]
// 	ngSet := newSet[int]()
// 	okSet := newSet[int]()
// 	for i := 0; i < m; i++ {
// 		in := getStrs()
// 		c := s2i(in[0])
// 		r := in[len(in)-1]
// 		keys := make([]int, c)
// 		for j := 0; j < c; j++ {
// 			keys[j] = s2i(in[j+1])
// 		}

// 		for _, key := range keys {
// 			if r == "x" {
// 				ngSet.add(key)
// 			} else {
// 				okSet.add(key)
// 			}
// 		}
// 	}

// 	oks := make([]int, 0)
// 	for k := range okSet.values {
// 		oks = append(oks, k)
// 	}
// 	oks = sortSlice(oks)

// 	ngs := make([]int, 0)
// 	for k := range ngSet.values {
// 		ngs = append(ngs, k)
// 	}
// 	ngs = sortSlice(ngs)

// 	okcombinationsCh := getCombinations(oks, k)
// 	okcombinations := make([][]int, 0)
// 	for okComb := range okcombinationsCh {
// 		okcombinations = append(okcombinations, okComb)
// 	}

// 	ngCombinations := make([][]int, 0)
// 	ngCombinasionsCh := getCombinations(ngs, k)
// 	for ngComb := range ngCombinasionsCh {
// 		ngCombinations = append(ngCombinations, ngComb)
// 	}

// 	fmt.Println(len(okcombinations) - len(ngCombinations))
// 	cnt := 0
// 	for _, comb := range okcombinations {
// 		flag := true
// 		for _, ngPair := range ngCombinations {
// 			if compareSlices(ngPair, comb) {
// 				flag = false
// 				break
// 			}
// 		}
// 		if flag {
// 			cnt++
// 		}
// 	}

// 	fmt.Println(cnt)
// }

// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

func getInt() int {
	return s2i(input())
}

func getInts() []int {
	return mapToIntSlice(input())
}

func getStr() string {
	return input()
}

func getStrs() []string {
	return strToSlice(input(), " ")
}

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

func getBigInt(x int) *big.Int {
	return big.NewInt(int64(x))
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

func pow(base, exp int) int {
	result := 1
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base)
		}
		base = (base * base)
		exp /= 2
	}
	return result
}

func modPow(base, exp, mod int) int {
	result := 1
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % mod
		}
		base = (base * base) % mod
		exp /= 2
	}
	return result
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

func ceilDiv(a, b int) int {
	if a + b - 1 < 0 && (a + b - 1) % b != 0 {
		return (a + b - 1) / b - 1
	}
	return (a + b - 1) / b
}

// set
type Set[V comparable] struct {
	values map[V]struct{}
}
func newSet[V comparable]() *Set[V] {
	return &Set[V]{values: make(map[V]struct{})}
}
func (s *Set[V]) add(v V) {
	s.values[v] = struct{}{}
}
func (s *Set[V]) remove(v V) {
	delete(s.values, v)
}
func (s *Set[V]) has(v V) bool {
	_, ok := s.values[v]
	return ok
}

// sorted set
type SortedSet[T comparator.Ordered] struct {
	values *set.Set[T]
}
func newSortedSet[T comparator.Ordered]() *SortedSet[T] {
	var comparatorFn comparator.Comparator[T] = comparator.OrderedTypeCmp[T]
	return &SortedSet[T]{values: set.New[T](comparatorFn)}
}
func (s *SortedSet[T]) add(v T) {
	s.values.Insert(v)
}
func (s *SortedSet[T]) remove(v T) {
	s.values.Erase(v)
}
func (s *SortedSet[T]) has(v T) bool {
	return s.values.Contains(v)
}
func (s *SortedSet[T]) size() int {
	return s.values.Size()
}
func (s *SortedSet[T]) lowerBound(v T) *set.SetIterator[T] {
	return s.values.LowerBound(v)
}
func (s *SortedSet[T]) upperBound(v T) *set.SetIterator[T] {
	return s.values.UpperBound(v)
}

// heap (priority queue)
// 1.21 以上になったら comp.Ordered に変更する
type Heap[T constraints.Ordered] []T
func (h Heap[T]) Len() int {
	return len(h)
}
func (h Heap[T]) Less(i, j int) bool {
	return h[i] < h[j]
}
func (h Heap[T]) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *Heap[T]) Push(x any) {
	*h = append(*h, x.(T))
}
func (h *Heap[T]) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MyHeap[T constraints.Ordered] struct {
	heap Heap[T]
}
func newMyHeap[T constraints.Ordered]() *MyHeap[T] {
	myHeap := &MyHeap[T]{}
	heap.Init(&myHeap.heap)
	return myHeap
}
func (h *MyHeap[T]) push(x T) {
	heap.Push(&h.heap, x)
}
func (h *MyHeap[T]) pop() T {
	return heap.Pop(&h.heap).(T)
}
func (h *MyHeap[T]) len() int {
	return h.heap.Len()
}

func sortSlice[T constraints.Ordered](slice []T) []T {
    copiedSlice := make([]T, len(slice))
    copy(copiedSlice, slice)

    sort.Slice(copiedSlice, func(i, j int) bool {
        return copiedSlice[i] < copiedSlice[j]
    })

    return copiedSlice
}

func reverse[T constraints.Ordered](slice []T) []T {
	copiedSlice := make([]T, len(slice))
	copy(copiedSlice, slice)

	for i, j := 0, len(copiedSlice)-1; i < j; i, j = i+1, j-1 {
		copiedSlice[i], copiedSlice[j] = copiedSlice[j], copiedSlice[i]
	}
	return copiedSlice
}

// 1.22 になったら slice.Contains を使用する
func sliceContains[T comparable](slice []T, v T) bool {
	for _, e := range slice {
		if e == v {
			return true
		}
	}
	return false
}

// queue
type Queue[T any] struct {
	values []T
}
func newQueue[T any]() *Queue[T] {
	return &Queue[T]{}
}
func (q *Queue[T]) push(v T) {
	q.values = append(q.values, v)
}
func (q *Queue[T]) popLeft() T {
	v := q.values[0]
	q.values = q.values[1:]
	return v
}
func (q *Queue[T]) pop() T {
	v := q.values[len(q.values)-1]
	q.values = q.values[:len(q.values)-1]
	return v
}
func (q *Queue[T]) front() T {
	return q.values[0]
}
func (q *Queue[T]) size() int {
	return len(q.values)
}
func (q *Queue[T]) empty() bool {
	return len(q.values) == 0
}

// UnionFind
type UnionFind struct {
	// parentsは要素が正の値のときはそのインデックスのルートを表す。
	// 負の値のときはそのインデックスはルートであり絶対値がそのルートが持つ要素数を表す。
	parents []int
}
func (uf *UnionFind) root(x int) int {
	if uf.parents[x] < 0 {
		return x
	}
	uf.parents[x] = uf.root(uf.parents[x])
	return uf.parents[x]
}
func (uf *UnionFind) unit(x, y int) {
	x = uf.root(x)
	y = uf.root(y)
	if x == y {
		return
	}
	// x, yはルートなので必ず負の値(そのルートがもつ要素数)になる
	if uf.parents[x] > uf.parents[y] {
		x, y = y, x
	}
	// ルートの要素数を更新
	uf.parents[x] += uf.parents[y]
	// サイズが小さい方のルートを大きい方のルートに繋げる
	uf.parents[y] = x
}
func (uf *UnionFind) isSame(x, y int) bool {
	return uf.root(x) == uf.root(y)
}
func (uf *UnionFind) size(x int) int {
	return -uf.parents[uf.root(x)]
}
func newUnionFind(n int) *UnionFind {
	parents := make([]int, n)
	for i := 0; i < n; i++ {
		parents[i] = -1
	}
	return &UnionFind{parents: parents}
}

// algorithm
// 約数列挙
func getDividors(n int) []int {
	ret := make([]int, 0)
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			ret = append(ret, i)
			if i*i != n {
				ret = append(ret, n/i)
			}
		}
	}
	return sortSlice(ret)
}

// 順列列挙
// 与えられたスライスの次の順列を取得する
// 使用例
// x := []int{1, 2, 3, 4}
// for {
// 	fmt.Println(x)
// 	if !NextPermutation(sort.IntSlice(x)) {
// 		break
// 	}
// }
func nextPermutation(x sort.Interface) bool {
	n := x.Len() - 1
	if n < 1 {
		return false
	}
	j := n - 1
	for ; !x.Less(j, j+1); j-- {
		if j == 0 {
			return false
		}
	}
	l := n
	for !x.Less(j, l) {
		l--
	}
	x.Swap(j, l)
	for k, l := j+1, n; k < l; {
		x.Swap(k, l)
		k++
		l--
	}
	return true
}

// 組み合わせ
// スライスからk個選ぶ組み合わせを列挙
func getCombinations(list []int, k int) (c chan []int) {
	c = make(chan []int, 2)
	n := len(list)

	pattern := make([]int, k)

	var body func(pos, begin int)
	body = func(pos, begin int) {
		if pos == k {
			t := make([]int, k)
			copy(t, pattern)
			c <- t
			return
		}

		for num := begin; num < n+pos-k+1; num++ {
			pattern[pos] = list[num]
			body(pos+1, num+1)
		}
	}
	go func() {
		defer close(c)
		body(0, 0)
	}()

	return
}

// nCr
func getComb(n, k int) (c chan []int) {
	pat := make([]int, k)
	c = make(chan []int, 1)

	var rec func(pos, start int)

	rec = func(pos, start int) {
		// k個選んでいれば、それを出力する
		if pos == k {
			tmp := make([]int, k)
			copy(tmp, pat)
			c <- tmp
			return
		}
		// 選んでいない場合は、追加して再帰
		// 次に選べるのは、startからn-1までの値のいずれか
		for i := start; i < n; i++ {
			pat[pos] = i    // posに選んだ数字をセットして
			rec(pos+1, i+1) // pos, startを１つずつ進める
		}
	}
	go func() {
		defer close(c)
		rec(0, 0)
	}()

	return
}

// n以下の素数を列挙
func primeNumbers(n int) []int {
	isPrime := make([]bool, n+1)
	for i := 0; i <= n; i++ {
		isPrime[i] = true
	}
	isPrime[0] = false
	isPrime[1] = false

	for i := 2; i <= n; i++ {
		if isPrime[i] {
			for j := i * 2; j <= n; j += i {
				isPrime[j] = false
			}
		}
	}

	primes := make([]int, 0)
	for i, b := range isPrime {
		if b {
			primes = append(primes, i)
		}
	}

	return primes
}


// binary search
func bisectLeft(slice []int, value int) int {
	return sort.Search(len(slice), func(i int) bool { return slice[i] >= value })
}
func bisectRight(slice []int, value int) int {
	return sort.Search(len(slice), func(i int) bool { return slice[i] > value })
}


