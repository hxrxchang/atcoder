package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var N int
	var S_ string
	fmt.Scan(&N)
	fmt.Scan(&S_)
	S := strings.Split(S_, "")
	tmp := S[0]
	for i := 1; i < len(S); i++ {
		if S[i] == tmp {
			fmt.Println("No")
			os.Exit(0)
		}
		tmp = S[i]
	}
	fmt.Println("Yes")
}
