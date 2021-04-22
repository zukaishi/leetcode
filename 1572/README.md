https://leetcode.com/problems/matrix-diagonal-sum/

```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = 0
        y = 0
        n = 0
        for i in range(0,len(mat)):
            x_max = len(mat) -1
            for j in range(0,len(mat[i])):
                xx = x_max -x
                n += mat[x][y]
                mat[x][y] = 0
                n += mat[i][xx]
                mat[i][xx] = 0
            x += 1
            y += 1
        return n        
```