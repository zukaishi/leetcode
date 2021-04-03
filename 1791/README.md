https://leetcode.com/problems/find-center-of-star-graph/

```go
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
```

```python
class Solution:
    def findCenter(self, edges) -> int:
        list = []
        ans = 0
        for v in edges:
            if v[0] in list:
                ans = v[0]
                break
            elif v[1] in list:
                ans = v[1]
            list.insert(0,v[0])
            list.insert(0,v[1])
        return ans
```