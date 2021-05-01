from typing import List
print("diStringMatch")

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        r = []
        low = 0
        up = len(s)
        for v in s:
            if v == "D":
                r.append(up)
                up -= 1
            else:
                r.append(low)
                low += 1
        r.append(up)
        return r

solution = Solution()
print(solution.diStringMatch("IDID"))