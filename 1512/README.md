https://leetcode.com/problems/number-of-good-pairs/

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = 0
        nums2 = set(nums)
        for i in nums2:
            count = nums.count(i)
            if count > 1:
                for j in range(count):
                    num += j
                
        return num
```