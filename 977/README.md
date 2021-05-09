https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = []
        for v in nums:
            r.append(v**2)
        return sorted(r)
```
