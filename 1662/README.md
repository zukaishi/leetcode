https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

```python
    def arrayStringsAreEqual(self, word1,word2) -> bool:
        return_bool = False
        if ''.join(word1) == ''.join(word2):
            return_bool = True
        return return_bool
```
