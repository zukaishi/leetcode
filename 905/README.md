https://leetcode.com/problems/sort-array-by-parity/

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        g = []
        k = []
        for v in A:
            if v % 2 == 0:
                g.append(v)
            else:
                k.append(v)
        return g + k
```