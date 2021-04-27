https://leetcode.com/problems/sum-of-digits-in-base-k/

```python
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        arr = []
        nn = n
        num = 0
        for _ in range(0,n):
            nn,kk = divmod(nn, k)
            arr.append(kk)
            if nn == 0:
                break
        for v in arr:
            num += int(v)
        return num
```
