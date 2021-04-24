https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

```python 
class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 != 0:
            arr.append(0)
        if n == 1:
            return arr
        max = 1000
        for _ in range(0,int(n/2)):
            arr.append(int(max))
            arr.append(int(max*-1))
            max -= 1
        return arr
```