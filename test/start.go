package main

import (
	"fmt"
)

func main() {
	fmt.Println("Go!!!")
	s := []int{1, 2, 3, 4}
	r := runningSum(s)
	fmt.Println(r)
}

func runningSum(nums []int) []int {
	s := make([]int, len(nums), len(nums))
	num := 0
	for i := 0; i < len(nums); i++ {
		s[i] = nums[i] + num
		num = s[i]
	}
	return s
}
