https://leetcode.com/problems/maximum-69-number/

```python
    def maximum69Number (self, num: int) -> int:
        max = num
        str_num = str(num)
        for i in range(0,len(str_num)):
            n = num
            x = 1 if i == len(str_num) else 10 ** (len(str_num)-1 - i)
            y = 3 if str_num[i] == "6" else -3
            n += x*y
            if n > max:
                max = n
        return max
```