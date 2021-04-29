https://leetcode.com/problems/sum-of-unique-elements/

```python
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        r = []
        for i in nums:
            if nums.count(i) == 1:
                r.append(i)
        return sum(r)
```
