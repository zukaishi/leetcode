https://leetcode.com/problems/check-if-n-and-its-double-exist/

```python
    def checkIfExist(self, arr) -> bool:
        check = False
        v_count = 0
        lista = []
        for v in arr:
            lista.append([v_count,v])
            v_count += 1
        print(lista)

        for i,v in lista:
            for i2,v2 in lista:
                if v == v2 * 2 and i != i2:
                    check = True
        return check
```