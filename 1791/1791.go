package main

import (
	"fmt"
)

func main() {
	fmt.Println("Go!!!")
	s := [][]int{{1, 2}, {2, 3}, {4, 2}}
	//fmt.Println(s)
	r := findCenter(s)
	fmt.Println(r)
}

func findCenter(edges [][]int) int {
	n1 := 0
	n2 := 0
	ans := 0
	for _, v := range edges {
		if n1 == v[0] || n2 == v[0] {
			ans = v[0]
			break
		} else if n1 == v[1] || n2 == v[1] {
			ans = v[1]
			break
		}
		if n1 == 0 {
			n1 = v[0]
		}
		if n2 == 0 {
			n2 = v[1]
		}
	}
	return ans
}
