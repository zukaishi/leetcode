from typing import List
print("countNegatives")

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num = 0
        for v in grid:
            for v2 in v:
                if v2 < 0:
                    num += 1
        return num


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
solution = Solution()
print(solution.countNegatives(grid))
