from typing import List
print("sortArrayByParity")

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        g = []
        k = []
        for v in A:
            if v % 2 == 0:
                g.append(v)
            else:
                k.append(v)
        return g + k

a =[3,1,2,4]
solution = Solution()
print(solution.sortArrayByParity(a))