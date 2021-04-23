https://leetcode.com/problems/determine-color-of-a-chessboard-square/

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return_bool = False
        if (ord(coordinates[0:1])-96)% 2 != int(coordinates[1:2]) % 2:
            return_bool = True
        return return_bool
```