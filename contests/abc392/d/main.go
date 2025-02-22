package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"math/big"
	"os"
	"sort"
	"strconv"
	"strings"

	"github.com/liyue201/gostl/ds/deque"
	"github.com/liyue201/gostl/ds/set"
	"github.com/liyue201/gostl/utils/comparator"
	"golang.org/x/exp/constraints"
	"golang.org/x/exp/maps"
)

const BUFSIZE = 10000000
const MOD = 1000000007
const BIGGEST = 1 << 60
const MINIMUM = -BIGGEST
var rdr *bufio.Reader

func main() {
	rdr = bufio.NewReaderSize(os.Stdin, BUFSIZE)
	solve()
}

func solve() {
	n := getInt()

	dices := make([]map[int]int, n)
	for i := 0; i < n; i++ {
		in := getInts()
		k, values := in[0], in[1:]
		dice := make(map[int]int)
		for j := 0; j < k; j++ {
			v := values[j]
			dice[v]++
		}
		dices[i] = dice
	}
}


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
	v, err := strconv.Atoi(s)
	if err != nil {
		panic("Faild : " + s + " can't convert to int")
	}
	return v
}

func s2float64(s string) float64 {
	v, err := strconv.ParseFloat(s, 64)
	if err != nil {
		panic("Faild : " + s + " can't convert to float64")
	}
	return v
}

func i2s(i int) string {
	return strconv.Itoa(i)
}

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
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

func i2bit(i int) []string {
	return strToSlice(strconv.FormatInt(int64(i), 2), "")
}

func bit2i(bits []string) int {
	bitStr := strings.Join(bits, "")

	result, err := strconv.ParseInt(bitStr, 2, 64)
	if err != nil {
		panic(err)
	}
	return int(result)
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

func sum(slice []int) int {
	sum := 0
	for _, v := range slice {
		sum += v
	}
	return sum
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

//----------------------------------------
// modint
//----------------------------------------
type modint struct {
	mod       int
	factMemo  []int
	ifactMemo []int
}

func newModint(m int) *modint {
	var ret modint
	ret.mod = m
	ret.factMemo = []int{1, 1}
	ret.ifactMemo = []int{1, 1}
	return &ret
}

func (m *modint) add(a, b int) int {
	ret := (a + b) % m.mod
	if ret < 0 {
		ret += m.mod
	}
	return ret
}

func (m *modint) sub(a, b int) int {
	ret := (a - b) % m.mod
	if ret < 0 {
		ret += m.mod
	}
	return ret
}

func (m *modint) mul(a, b int) int {
	a %= m.mod
	b %= m.mod
	ret := a * b % m.mod
	if ret < 0 {
		ret += m.mod
	}
	return ret
}

func (m *modint) div(a, b int) int {
	a %= m.mod
	ret := a * m.modinv(b)
	ret %= m.mod
	return ret
}

func (m *modint) pow(p, n int) int {
	ret := 1
	x := p % m.mod
	for n != 0 {
		if n%2 == 1 {
			ret *= x
			ret %= m.mod
		}
		n /= 2
		x = x * x % m.mod
	}
	return ret
}


// 拡張オイラーの互除法で逆元を求める
func (mm *modint) modinv(a int) int {
	m := mm.mod
	b, u, v := m, 1, 0
	for b != 0 {
		t := a / b
		a -= t * b
		a, b = b, a
		u -= t * v
		u, v = v, u
	}
	u %= m
	if u < 0 {
		u += m
	}
	return u
}

//-----------------------------------------------
// 行列累乗
// 　A[][]のp乗を求める
//-----------------------------------------------
func (m *modint) powModMatrix(A [][]int, p int) [][]int {
	N := len(A)
	ret := make([][]int, N)
	for i := 0; i < N; i++ {
		ret[i] = make([]int, N)
		ret[i][i] = 1
	}

	for p > 0 {
		if p&1 == 1 {
			ret = m.mulMod(ret, A)
		}
		A = m.mulMod(A, A)
		p >>= 1
	}

	return ret
}

func (m *modint) mulMod(A, B [][]int) [][]int {
	H := len(A)
	W := len(B[0])
	K := len(A[0])
	C := make([][]int, W)
	for i := 0; i < W; i++ {
		C[i] = make([]int, W)
	}

	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			for k := 0; k < K; k++ {
				C[i][j] += A[i][k] * B[k][j]
				C[i][j] %= m.mod
			}
		}
	}

	return C
}

//---------------------------------------------------
// nCk 計算関連：　TLEすることがあるかも
//                ※pow(x, p-2)を何度も取るので
// 厳しそうな場合は、ここを削除して高速なのを使う
//---------------------------------------------------
func (m *modint) mfact(n int) int {
	if len(m.factMemo) > n {
		return m.factMemo[n]
	}
	if len(m.factMemo) == 0 {
		m.factMemo = append(m.factMemo, 1)
	}
	for len(m.factMemo) <= n {
		size := len(m.factMemo)
		m.factMemo = append(m.factMemo, m.factMemo[size-1]*size%m.mod)
	}
	return m.factMemo[n]
}

func (m *modint) mifact(n int) int {
	if len(m.ifactMemo) > n {
		return m.ifactMemo[n]
	}
	if len(m.ifactMemo) == 0 {
		m.factMemo = append(m.ifactMemo, 1)
	}
	for len(m.ifactMemo) <= n {
		size := len(m.ifactMemo)
		m.ifactMemo = append(m.ifactMemo, m.ifactMemo[size-1]*m.pow(size, m.mod-2)%m.mod)
	}
	return m.ifactMemo[n]
}

func (m *modint) nCr(n, r int) int {
	if n == r {
		return 1
	}
	if n < r || r < 0 {
		return 0
	}
	ret := 1
	ret *= m.mfact(n)
	ret %= m.mod
	ret *= m.mifact(r)
	ret %= m.mod
	ret *= m.mifact(n - r)
	ret %= m.mod
	return (ret)
}

// -----------------------------------------------

// logXのYを求める
func logXY(x, y int) int {
	return int(math.Log(float64(y)) / math.Log(float64(x)))
}

// intのまま計算できるように
func sqrt(x int) int {
	return int(math.Sqrt(float64(x)))
}

// xのn乗根
func rootN(x, n int) float64 {
	return math.Pow(float64(x), 1.0/float64(n))
}

// 最大公約数
func gcd(v1, v2 int) int {
	if v1 > v2 {
		v1, v2 = v2, v1
	}
	for v1 != 0 {
		v1, v2 = v2%v1, v1
	}
	return v2
}

// 最小公倍数
func lcm(v1, v2 int) int {
	return v1 * v2 / gcd(v1, v2)
}

// 切り上げ除算
func ceilDiv(a, b int) int {
	if a + b - 1 < 0 && (a + b - 1) % b != 0 {
		return (a + b - 1) / b - 1
	}
	return (a + b - 1) / b
}

// n以上の整数の中で、mの倍数で最小の値
func smallestMultiple(n, m int) int {
	if n % m == 0 {
		return n
	}
	if n > 0 {
		return n + m - n % m
	}
	return n - n % m
}

// n以下の整数の中で、mの倍数で最大の値
func largestMultiple(n, m int) int {
	if n % m == 0 {
		return n
	}
	if n > 0 {
		return n - n % m
	}
	return n - m - n % m
}

// nCr
func getComb(n, k int) int {
	numerator := 1
	denominator := 1
	for i := 0; i < k; i++ {
		numerator *= n - i
		denominator *= i + 1
	}
	return numerator / denominator
}

// nを素因数分解
func primeFactorize(n int) []int {
	var factors []int

	// 2で割り切れる間、2を追加
	for n%2 == 0 {
		factors = append(factors, 2)
		n /= 2
	}

	// 3以降の奇数で割り切れるか確認
	for f := 3; f*f <= n; f += 2 {
		for n%f == 0 {
			factors = append(factors, f)
			n /= f
		}
	}

	// nが1でない場合は、n自身を追加
	if n > 1 {
		factors = append(factors, n)
	}

	return factors
}

// n以下の素数を列挙
func primeNumbers(n int) []int {
	isPrime := getIsPrime(n)

	primes := make([]int, 0)
	for i, b := range isPrime {
		if b {
			primes = append(primes, i)
		}
	}

	return primes
}

// n以下の数字がそれぞれ素数かどうかを列挙
func getIsPrime(n int) []bool {
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
	return isPrime
}

// nが素数かどうかを判定
func isPrime(n int) bool {
	if n == 2 {
		return true
	} else if n < 2 || n%2 == 0 {
		return false
	}
	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// 2次元累積和
type PrefixSum2D struct {
	grid       [][]int
	prefixSum  [][]int
}
func NewPrefixSum2D(grid [][]int) *PrefixSum2D {
	n := len(grid)
	m := len(grid[0])

	prefixSum := make([][]int, n+1)
	for i := range prefixSum {
		prefixSum[i] = make([]int, m+1)
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			prefixSum[i][j] = grid[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
		}
	}

	return &PrefixSum2D{
		grid:      grid,
		prefixSum: prefixSum,
	}
}

func (ps *PrefixSum2D) Query(x1, y1, x2, y2 int) int {
	return ps.prefixSum[x2+1][y2+1] - ps.prefixSum[x1][y2+1] - ps.prefixSum[x2+1][y1] + ps.prefixSum[x1][y1]
}

// 整数nが桁数を満たさなかったら0埋めする
func zeroPad(n, digits int) string {
	return fmt.Sprintf("%0*d", digits, n)
}

// set
type Set[V comparable] struct {
	values map[V]struct{}
}
func newSet[V comparable]() *Set[V] {
	return &Set[V]{values: make(map[V]struct{})}
}
func (s *Set[V]) Add(v V) {
	s.values[v] = struct{}{}
}
func (s *Set[V]) Remove(v V) {
	delete(s.values, v)
}
func (s *Set[V]) Has(v V) bool {
	_, ok := s.values[v]
	return ok
}
func (s *Set[V]) Values() []V {
	return maps.Keys(s.values)
}
func (s *Set[V]) Size() int {
	return len(s.values)
}
func(s *Set[V]) Pop() V {
	if len(s.values) == 0 {
		panic("set is empty")
	}
	v := s.Values()[0]
	s.Remove(v)
	return v
}


// sorted set
type SortedSet[T comparator.Ordered] struct {
	*set.Set[T]
}
func newSortedSet[T comparator.Ordered]() *SortedSet[T] {
	var comparatorFn comparator.Comparator[T] = comparator.OrderedTypeCmp[T]
	return &SortedSet[T]{set.New[T](comparatorFn)}
}
func (s *SortedSet[T]) add(v T) {
	s.Insert(v)
}
func (s *SortedSet[T]) remove(v T) {
	s.Erase(v)
}
func (s *SortedSet[T]) has(v T) bool {
	return s.Contains(v)
}
func (s *SortedSet[T]) size() int {
	return s.Size()
}
func (s *SortedSet[T]) lowerBound(v T) *set.SetIterator[T] {
	return s.LowerBound(v)
}
func (s *SortedSet[T]) upperBound(v T) *set.SetIterator[T] {
	return s.UpperBound(v)
}
// 指定した値未満の最大の値を取得
func (s *SortedSet[T]) lessThan(v T) (*T, error) {
	if s.lowerBound(v).Prev().IsValid() {
		res := s.lowerBound(v).Prev().Value()
		return &res, nil
	}
	if s.Last().IsValid() {
		res := s.Last().Value()
		if res < v {
			return &res, nil
		}
		return nil, fmt.Errorf("not found")
	}
	return nil, fmt.Errorf("not found")
}

type MultiSet[T comparable] struct {
	*set.MultiSet[T]
	mapping map[T]int
}
// multiset
func newMultiset[T comparator.Ordered]() *MultiSet[T] {
	var comparatorFn comparator.Comparator[T] = comparator.OrderedTypeCmp[T]
	ms := set.NewMultiSet[T](comparatorFn, set.WithGoroutineSafe())
	return &MultiSet[T]{MultiSet: ms, mapping: make(map[T]int)}
}
func (ms *MultiSet[T]) Add(v T) {
	ms.Insert(v)
	ms.mapping[v]++
}
func (ms *MultiSet[T]) Remove(v T) {
	ms.mapping[v] = max(0, ms.mapping[v] - 1)
	if ms.mapping[v] == 0 {
		ms.Erase(v)
	}
}
func (ms *MultiSet[T]) Has(v T) bool {
	return ms.Contains(v)
}

// heap (priority queue)
// 1.21 以上になったら cmp.Ordered に変更する
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

// tuple heap
type TupleHeap[T constraints.Ordered] [][]T
func (th TupleHeap[T]) Len() int {
	return len(th)
}
func (th TupleHeap[T]) Less(i, j int) bool {
	return th.compareSlices(i, j, 0)
}
func (th TupleHeap[T]) Swap(i, j int) {
	th[i], th[j] = th[j], th[i]
}
func (th *TupleHeap[T]) Push(x any) {
	*th = append(*th, x.([]T))
}
func (h *TupleHeap[T]) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func (th TupleHeap[T]) compareSlices(i, j, idx int) bool {
	a := th[i]
	b := th[j]
	// 片方のスライスが他方よりも短ければ、その時点で比較を終了
	if len(a) <= idx && len(b) > idx {
		return true
	} else if len(a) > idx && len(b) <= idx {
		return false
	} else if len(a) <= idx && len(b) <= idx {
		return false // どちらも同じ長さで全ての要素が等しい場合
	}

	// 現在のインデックスの値を比較
	if a[idx] != b[idx] {
		return a[idx] < b[idx]
	}

	// 同じ値の場合、次のインデックスを再帰的に比較
	return th.compareSlices(i, j, idx+1)
}

type MyTupleHeap[T constraints.Ordered] struct {
	heap TupleHeap[T]
}
func newMyTupleHeap[T constraints.Ordered]() *MyTupleHeap[T] {
	myTupleHeap := &MyTupleHeap[T]{}
	heap.Init(&myTupleHeap.heap)
	return myTupleHeap
}
func (h *MyTupleHeap[T]) push(x []T) {
	heap.Push(&h.heap, x)
}
func (h *MyTupleHeap[T]) pop() []T {
	return heap.Pop(&h.heap).([]T)
}
func (h *MyTupleHeap[T]) len() int {
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

func descendingSortSlice[T constraints.Ordered](slice []T) []T {
	copiedSlice := make([]T, len(slice))
	copy(copiedSlice, slice)

	sort.Slice(copiedSlice, func(i, j int) bool {
		return copiedSlice[i] > copiedSlice[j]
	})

	return copiedSlice
}

func reverse[T any](slice []T) []T {
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

// 0~n-1までのスライスを作成
func rangeSlice(n int) []int {
	slice := make([]int, n)
	for i := 0; i < n; i++ {
		slice[i] = i
	}
	return slice
}

// 開区間でstart~endまでのスライスを作成
func rangeSlice2(start, end int) []int {
	slice := make([]int, end - start + 1)
	for i := start; i <= end; i++ {
		slice[i - start] = i
	}
	return slice
}

// intのsliceを0indexに変換
func zeroIndexedSlice(origin []int) []int {
	slice2 := make([]int, len(origin))
	for i, v := range origin {
		slice2[i] = v - 1
	}
	return slice2
}

func copySlice[T any](original []T) []T {
	newSlice := make([]T, len(original))
	copy(newSlice, original)
	return newSlice
}

// 2次元スライスのコピー
func copy2DSlice[T any](original [][]T) [][]T {
    newSlice := make([][]T, len(original))
    for i := range original {
        newSlice[i] = make([]T, len(original[i]))
        copy(newSlice[i], original[i])
    }
    return newSlice
}

// スライスを指定した位置で分割して逆順に結合
func splitAndReverse[T any](slice []T, index int) []T {
    if index < 0 || index >= len(slice) {
        panic("index out of range")
    }
    front := slice[:index]
    back := slice[index:]

    return append(back, front...)
}


// スライスを文字列に変換
func sliceToStr[T any](data []T, separator string) string {
	var strSlice []string
    for _, v := range data {
        strSlice = append(strSlice, fmt.Sprintf("%v", v))
    }
    return strings.Join(strSlice, separator)
}

// n以上m以下の平方数を列挙
func findSquaresInRange(n, m int) []int {
	start := int(math.Ceil(math.Sqrt(float64(n))))
	end := int(math.Floor(math.Sqrt(float64(m))))
	result := []int{}
	for i := start; i <= end; i++ {
		result = append(result, i*i)
	}
	return result
}

// queue
func newQueue[T any]() *deque.Deque[T] {
	return deque.New[T]()
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
// 	if !nextPermutation(sort.IntSlice(x)) {
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
func getCombinations(list []int, k int) [][]int {
	res := make([][]int, 0)
	combs := getCombinationsCh(list, k)
	for comb := range combs {
		res = append(res, comb)
	}
	return res
}
func getCombinationsCh(list []int, k int) (c chan []int) {
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

// bit全探索
func generateSubsets[T any](elements []T) [][]T {
	n := len(elements)
	totalCombinations := 1 << n
	subsets := make([][]T, totalCombinations)

	for i := 0; i < totalCombinations; i++ {
		var subset []T
		for j := 0; j < n; j++ {
			if i&(1<<j) != 0 {
				subset = append(subset, elements[j])
			}
		}
		subsets[i] = subset
	}

	return subsets
}

// binary search
func binarySearch[T constraints.Ordered](slice []T, fn func(int) bool) int {
	return sort.Search(len(slice), fn)
}
// sliceの中でvalue以上の値が最初に現れるindexを返す
func lowerBound[T constraints.Ordered](slice []T, value T) int {
	return binarySearch(slice, func(i int) bool { return slice[i] >= value })
}
// sliceの中でvalueより大きい値が最初に現れるindexを返す
func upperBound[T constraints.Ordered](slice []T, value T) int {
	return binarySearch(slice, func(i int) bool { return slice[i] > value })
}
// sliceの中で指定した値以上の最小の要素を返す
func equalOrMoreThan[T constraints.Ordered](slice []T, value T) *T {
	idx := lowerBound(slice, value)
	if slice[idx] == value {
		return &value
	}
	if idx == 0 {
		return nil
	}
	return &slice[idx-1]
}
// sliceの中で指定した値以下の最大の要素を返す
func equalOrLessThan[T constraints.Ordered](slice []T, value T) *T {
	idx := upperBound(slice, value)
	if idx == 0 {
		return nil
	}
	return &slice[idx-1]
}
// sliceの中で指定した値より大きい要素を返す
func moreThan[T constraints.Ordered](slice []T, value T) *T {
	idx := upperBound(slice, value)
	if idx < len(slice) {
		return &slice[idx]
	}
	return nil
}
// sliceの中で指定した値未満の中で最大の要素を返す
func lessThan[T constraints.Ordered](slice []T, value T) *T {
	idx := lowerBound(slice, value)
	if idx == 0 {
		return nil
	}
	return &slice[idx-1]
}

// 座標圧縮
type Zaatsu struct {
	values []int
	mapping map[int]int
}
func newZaatsu(params []int) *Zaatsu {
	s := newSet[int]()
	for _, v := range params {
		s.Add(v)
	}
	sorted := sortSlice(s.Values())

	mapping := make(map[int]int)
	for i, v := range sorted {
		mapping[v] = i
	}

	return &Zaatsu{
		values: sorted,
		mapping: mapping,
	}
}
// 圧縮後の値を取得
func (z *Zaatsu) GetCompressedValue(v int) int {
	if val, ok := z.mapping[v]; !ok {
		panic("value not found")
	} else {
		return val
	}
}
// 圧縮後の値から元の値を取得
func (z *Zaatsu) GetOriginalValue(compressedIndex int) int {
	if compressedIndex < 0 || compressedIndex >= len(z.values) {
		panic("Index out of range")
	}
	return z.values[compressedIndex]
}
func (z *Zaatsu) Count() int {
	return len(z.values)
}
func (z *Zaatsu) LowerBound(v int) int {
	return lowerBound(z.values, v)
}
func (z *Zaatsu) UpperBound(v int) int {
	return upperBound(z.values, v)
}

// セグメント木
type SegmentTree[T any] struct {
	data []T
	n    int // 葉の数(全区間の要素数)
	e    T // 単位元
	op   func(T, T) T
}

func NewSegmentTree[T any](n int, e T, op func(T, T) T) *SegmentTree[T] {
	segtree := &SegmentTree[T]{}
	segtree.e = e
	segtree.op = op
	segtree.n = 1
	for segtree.n < n {
		segtree.n *= 2
	}
	segtree.data = make([]T, segtree.n*2-1)
	for i := 0; i < segtree.n*2-1; i++ {
		segtree.data[i] = segtree.e
	}
	return segtree
}

func (segtree *SegmentTree[T]) Update(idx int, x T) {
	idx += segtree.n - 1
	segtree.data[idx] = x
	for 0 < idx {
		idx = (idx - 1) / 2
		segtree.data[idx] = segtree.op(segtree.data[idx*2+1], segtree.data[idx*2+2])
	}
}

func (segtree *SegmentTree[T]) query(begin, end, idx, a, b int) T {
	if b <= begin || end <= a {
		return segtree.e
	}
	if begin <= a && b <= end {
		return segtree.data[idx]
	}
	v1 := segtree.query(begin, end, idx*2+1, a, (a+b)/2)
	v2 := segtree.query(begin, end, idx*2+2, (a+b)/2, b)
	return segtree.op(v1, v2)
}
// endは閉区間であることに注意
func (segtree *SegmentTree[T]) Query(begin, end int) T {
	return segtree.query(begin, end, 0, 0, segtree.n)
}

// 遅延評価セグメント木
type LazySegmentTree struct {
	data   []int
	lazy   []int
	n      int
	op     func(int, int) int
	noop   int
	lazyOp func(int, int) int
	isNoop func(int) bool
}

func NewLazySegmentTree(n int, op, lazyOp func(int, int) int, noop int) *LazySegmentTree {
	seg := &LazySegmentTree{}
	seg.n = 1
	for seg.n < n {
		seg.n *= 2
	}
	seg.data = make([]int, seg.n*2-1)
	seg.lazy = make([]int, seg.n*2-1)
	seg.noop = noop
	seg.op = op
	seg.lazyOp = lazyOp

	isNoop := func(x int) bool {
		return x == noop
	}
	seg.isNoop = isNoop
	return seg
}

func (seg *LazySegmentTree) eval(idx, l, r int) {
	if !seg.isNoop(seg.lazy[idx]) {
		seg.data[idx] = seg.lazyOp(seg.data[idx], seg.lazy[idx]*(r-l))
		if r-l > 1 {
			seg.lazy[idx*2+1] = seg.lazyOp(seg.lazy[idx*2+1], seg.lazy[idx])
			seg.lazy[idx*2+2] = seg.lazyOp(seg.lazy[idx*2+2], seg.lazy[idx])
		}
		seg.lazy[idx] = seg.noop
	}
}

func (seg *LazySegmentTree) UpdateRange(begin, end, x int) {
	seg.updateRange(begin, end, 0, 0, seg.n, x)
}

func (seg *LazySegmentTree) updateRange(begin, end, idx, l, r, x int) {
	seg.eval(idx, l, r)
	if end <= l || r <= begin {
		return
	}
	if begin <= l && r <= end {
		seg.lazy[idx] = seg.lazyOp(seg.lazy[idx], x)
		seg.eval(idx, l, r)
	} else {
		seg.updateRange(begin, end, idx*2+1, l, (l+r)/2, x)
		seg.updateRange(begin, end, idx*2+2, (l+r)/2, r, x)
		seg.data[idx] = seg.op(seg.data[idx*2+1], seg.data[idx*2+2])
	}
}

func (seg *LazySegmentTree) Query(begin, end int) int {
	return seg.query(begin, end, 0, 0, seg.n)
}

func (seg *LazySegmentTree) query(begin, end, idx, l, r int) int {
	seg.eval(idx, l, r)
	if end <= l || r <= begin {
		return 0
	}
	if begin <= l && r <= end {
		return seg.data[idx]
	}
	v1 := seg.query(begin, end, idx*2+1, l, (l+r)/2)
	v2 := seg.query(begin, end, idx*2+2, (l+r)/2, r)
	return seg.op(v1, v2)
}


// 単純なgraphのDFS
func graphBfs(graph [][]int, start int) []int {
	size := len(graph)
	que := newQueue[int]()
	distances := make([]int, size)
	for i := 0; i < size; i++ {
		distances[i] = -1
	}
	distances[start] = 0
	que.PushBack(start)
	for que.Size() > 0 {
		v := que.PopFront()
		for _, next := range graph[v] {
			if distances[next] != -1 {
				continue
			}
			distances[next] = distances[v] + 1
			que.PushBack(next)
		}
	}
	return distances
}

// gridのDFS
type GridBfsNode struct {
	y, x int
}
func gridBfs(height, width int, nextNodes map[GridBfsNode][]GridBfsNode, start GridBfsNode) [][]int {
	type Item struct {
		item GridBfsNode
		dist int
	}
	distances := make([][]int, height)
	for i := 0; i < height; i++ {
		distances[i] = make([]int, width)
		for j := 0; j < width; j++ {
			distances[i][j] = -1
		}
	}

	distances[start.y][start.x] = 0

	que := newQueue[Item]()
	que.PushBack(Item{GridBfsNode{start.y, start.x}, 0})

	for que.Size() > 0 {
		current := que.PopFront()
		y, x, dist := current.item.y, current.item.x, current.dist
		for _, next := range nextNodes[GridBfsNode{y, x}] {
			if next.y < 0 || next.y >= height || next.x < 0 || next.x >= width {
				continue
			}
			if distances[next.y][next.x] != -1 {
				continue
			}
			distances[next.y][next.x] = dist + 1
			que.PushBack(Item{next, dist + 1})
		}
	}

	return distances
}

// ワーシャルフロイド法
// graphは、到達不能な場合はmath.MaxInt64を入れる
// 自分自身への経路は0を入れる
func warshallFloyd(graph [][]int) [][]int {
	// ノード数
	n := len(graph)

	// 結果を格納するために元のグラフをコピー
	dist := make([][]int, n)
	for i := 0; i < n; i++ {
		dist[i] = make([]int, n)
		copy(dist[i], graph[i])
	}

	// ワーシャル–フロイド法の計算
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				// 中継ノードを経由する距離が無限大でない場合に更新
				if dist[i][k] != BIGGEST && dist[k][j] != BIGGEST {
					dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
				}
			}
		}
	}

	return dist
}

// ダイクストラ法
func dijkstra(graph [][]dijkstraItem, start int) []int {
	n := len(graph)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = BIGGEST
	}

	// スタート地点からスタート地点自身への辺があった場合、それを優先する
	for _, edge := range graph[start] {
		if edge.node == start {
			dist[start] = min(dist[start], edge.dist)
		}
	}

	// なければ0
	if dist[start] == BIGGEST {
		dist[start] = 0
	}

	pq := &dijkstraPriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, &dijkstraItem{node: start, dist: 0})

	for pq.Len() > 0 {
		u := heap.Pop(pq).(*dijkstraItem)
		if u.dist > dist[u.node] {
			continue
		}

		for _, edge := range graph[u.node] {
			v := edge.node
			alt := u.dist + edge.dist
			if alt < dist[v] {
				dist[v] = alt
				heap.Push(pq, &dijkstraItem{node: v, dist: alt})
			}
		}
	}

	return dist
}
type dijkstraItem struct {
	node int
	dist   int
}
type dijkstraPriorityQueue []*dijkstraItem
func (pq dijkstraPriorityQueue) Len() int { return len(pq) }
func (pq dijkstraPriorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
}
func (pq dijkstraPriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}
func (pq *dijkstraPriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(*dijkstraItem))
}
func (pq *dijkstraPriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

// 有向グラフの強連結成分分解
func findSCCs(graph [][]int) [][]int {
	n := len(graph)
	visited := make([]bool, n)
	finishOrder := []int{}

	// 1. 一度目のDFSでノードを探索し、終了時間順にノードを記録
	var dfs1 func(v int)
	dfs1 = func(v int) {
		visited[v] = true
		for _, to := range graph[v] {
			if !visited[to] {
				dfs1(to)
			}
		}
		finishOrder = append(finishOrder, v)
	}

	for i := 0; i < n; i++ {
		if !visited[i] {
			dfs1(i)
		}
	}

	// 2. グラフを転置
	reversedGraph := make([][]int, n)
	for v, edges := range graph {
		for _, to := range edges {
			reversedGraph[to] = append(reversedGraph[to], v)
		}
	}

	// 3. 転置グラフで二度目のDFSを行い、強連結成分を収集
	var sccs [][]int
	visited = make([]bool, n)

	var dfs2 func(v int, component *[]int)
	dfs2 = func(v int, component *[]int) {
		visited[v] = true
		*component = append(*component, v)
		for _, to := range reversedGraph[v] {
			if !visited[to] {
				dfs2(to, component)
			}
		}
	}

	// finishOrderを逆順で処理
	for i := len(finishOrder) - 1; i >= 0; i-- {
		v := finishOrder[i]
		if !visited[v] {
			var component []int
			dfs2(v, &component)
			sccs = append(sccs, component)
		}
	}

	return sccs
}


// functional graphのサイクルを検出
func findCycle(n int, graph []int) (*[]int, error) {
	visited := make([]int, n) // 0: 未訪問, 1: 訪問中, 2: 訪問完了
	start, end := -1, -1

	// DFSでサイクルを検出
	var dfs func(v int) bool
	dfs = func(v int) bool {
		if visited[v] == 1 { // サイクル検出
			start = v
			end = v
			return true
		}
		if visited[v] == 2 { // 訪問済み
			return false
		}
		visited[v] = 1
		next := graph[v]
		if dfs(next) {
			if start != -1 {
				if v == end { // サイクル終了点
					start = -1 // 全サイクルを検出終了
				}
				return true
			}
		}
		visited[v] = 2
		return false
	}

	// 全頂点についてDFSを試みる
	for i := 0; i < n; i++ {
		if visited[i] == 0 {
			if dfs(i) {
				break
			}
		}
	}

	// サイクルの頂点を抽出
	if end == -1 {
		return nil, fmt.Errorf("No cycle") // サイクルが存在しない場合
	}
	cycle := []int{end}
	for v := graph[end]; v != end; v = graph[v] {
		cycle = append(cycle, v)
	}
	return &cycle, nil
}

// ローリングハッシュ
func NewRollingHash(S string) *RollingHash {
	const base1, base2 = 1007, 2009
	const mod1, mod2 = 1000000007, 1000000009

	n := len(S)
	hash1 := make([]int64, n+1)
	hash2 := make([]int64, n+1)
	power1 := make([]int64, n+1)
	power2 := make([]int64, n+1)
	power1[0], power2[0] = 1, 1

	for i := 0; i < n; i++ {
		hash1[i+1] = (hash1[i]*base1 + int64(S[i])) % mod1
		hash2[i+1] = (hash2[i]*base2 + int64(S[i])) % mod2
		power1[i+1] = (power1[i] * base1) % mod1
		power2[i+1] = (power2[i] * base2) % mod2
	}

	return &RollingHash{
		base1:  base1,
		base2:  base2,
		mod1:   mod1,
		mod2:   mod2,
		hash1:  hash1,
		hash2:  hash2,
		power1: power1,
		power2: power2,
	}
}
type RollingHash struct {
	base1, base2 int64
	mod1, mod2   int64
	hash1, hash2 []int64
	power1, power2 []int64
}
type RollingHashPair struct {
	Hash1 int64
	Hash2 int64
}
// S[left:right] のハッシュ値を取得
func (rh *RollingHash) Get(l, r int) RollingHashPair {
	res1 := (rh.hash1[r] - rh.hash1[l]*rh.power1[r-l]%rh.mod1 + rh.mod1) % rh.mod1
	res2 := (rh.hash2[r] - rh.hash2[l]*rh.power2[r-l]%rh.mod2 + rh.mod2) % rh.mod2
	return RollingHashPair{res1, res2}
}


// sliceを一行で出力
func printSlice[T any](data []T) {
	fmt.Println(strings.Trim(fmt.Sprint(data), "[]"))
}

// 部分文字列判定
// 非連続の部分文字列も対応
// isSubstring("abcd", "ad") -> true
func isSubstring(s, t string) bool {
	ok := false
	iter := 0
	for i := 0; i < len(s); i++ {
		if s[i] == t[iter] {
			iter++
		}
		if iter == len(t) {
			ok = true
			break
		}
	}
	return ok
}

// 文字列を昇順でソート
func sortString(s string) string {
	runes := []rune(s)

	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})

	return string(runes)
}

// 文字列を降順でソート
func descendingSortString(s string) string {
	runes := []rune(s)

	sort.Slice(runes, func(i, j int) bool {
		return runes[i] > runes[j]
	})

	return string(runes)
}

// 文字列の更新
func updateString(s string, idx int, c byte) string {
	runes := []rune(s)
	runes[idx] = rune(c)
	return string(runes)
}

// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//　幾何ゾーン

// 2点間の距離
func distance(x1, y1, x2, y2 int) float64 {
	x1f := float64(x1)
	y1f := float64(y1)
	x2f := float64(x2)
	y2f := float64(y2)
	return math.Sqrt((x2f-x1f)*(x2f-x1f) + (y2f-y1f)*(y2f-y1f))
}

// 2点間の距離の2乗
// 平方根を取ると距離になるが、誤差が出るので距離の比較は距離の2乗で行う
func distanceSquared(x1, y1, x2, y2 int) int {
	return pow(x1-x2, 2) + pow(y1-y2, 2)
}

// 3点が同一直線上にあるか判定
func isOnSameLine(x1, y1, x2, y2, x3, y3 int) bool {
	return (x1-x2)*(y2-y3) == (y1-y2)*(x2-x3)
}
