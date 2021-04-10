https://leetcode.com/problems/xor-operation-in-an-array/

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return_num = 0
        for i in range(n):
            num = start + 2 * i
            return_num ^= num
        return return_num
```