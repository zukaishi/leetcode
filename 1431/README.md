https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

```go
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
```