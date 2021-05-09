from typing import List
print("sortedSquares")

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = []
        for v in nums:
            r.append(v**2)
        return sorted(r)

nums = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(nums))