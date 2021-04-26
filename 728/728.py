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
                for j in range(0,len(str_i)):
                    print(str_i[j])
        return r
solution = Solution()
print(solution.selfDividingNumbers(1,22))
