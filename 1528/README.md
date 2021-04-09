https://leetcode.com/problems/shuffle-string/

```python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str = ""
        strlist = {}
        for v in range(len(indices)):
            strlist[indices[v]] = s[v]
        strlist = sorted(strlist.items())
        for v in strlist:
            str += v[1]
        return str
```
