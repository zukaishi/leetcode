https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        r = ""
        for v in s.split():
            for i in range(len(v)-1,-1,-1):
                r += v[i]
            r += " "
        return r.strip(" ")
```