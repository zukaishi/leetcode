https://leetcode.com/problems/shuffle-the-array/submissions/

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        rlist = []
        for _ in nums:
            rlist = rlist + nums[i:i+1:1]
            rlist = rlist + nums[n+i:n+i+1:1]
            i += 1
            if i >= n:
                break
        return rlist
```