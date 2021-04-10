https://leetcode.com/problems/split-a-string-in-balanced-strings/

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return_num = 0
        r_count = 0
        l_count = 0
        for v in s:
            if v == "R":
                r_count += 1
            elif v == "L":
                l_count += 1
            if r_count == l_count:
                return_num += 1
                r_count =0
                l_count = 0
        return return_num        
```