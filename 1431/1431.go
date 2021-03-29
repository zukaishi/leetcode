package main

import (
	"fmt"
)

func main() {
	fmt.Println("Go!!!")
	s := []int{4, 2, 1, 1, 2}
	i := 1
	r := kidsWithCandies(s, i)
	fmt.Println(r)
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	s := make([]bool, len(candies), len(candies))
	max := 0
	for _, v := range candies {
		if v > max {
			max = v
		}
	}
	for i, v := range candies {
		if v+extraCandies >= max {
			s[i] = true
		} else {
			s[i] = false
		}
	}
	return s
}
