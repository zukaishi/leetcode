https://leetcode.com/problems/richest-customer-wealth/

```python
    def maximumWealth(self, accounts) -> int:
        max = 0
        for v in accounts:
            s = sum(v)
            if s > max:
                max = s
        return max

```