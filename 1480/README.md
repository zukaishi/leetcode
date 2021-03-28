https://leetcode.com/problems/running-sum-of-1d-array/

```go
	s := make([]int, len(nums), len(nums))
	num := 0
	for i := 0; i < len(nums); i++ {
		s[i] = nums[i] + num
		num = s[i]
	}
	return s
```