from typing import List
print("heightChecker")

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        r = 0
        heights_s =  sorted(heights)
        for i in range(0,len(heights)):
            if heights[i] != heights_s[i]:
                r += 1
        return r

heights = [5,1,2,3,4]
solution = Solution()
print(solution.heightChecker(heights))