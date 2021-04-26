from typing import List
print("selfDividingNumbers")

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left,right+1):
            if i < 10:
                r.append(i)
            else:
                str_i = str(i)
                n = 0
                for j in range(0,len(str_i)):
                    if str_i[j] != "0":
                        if i % int(str_i[j]) == 0:
                            n += 1
                if n == len(str_i):
                    r.append(i)
        return r
solution = Solution()
print(solution.selfDividingNumbers(1,22))
