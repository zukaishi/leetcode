
from typing import List
print("sumOfUnique")

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        r = []
        for i in nums:
            if nums.count(i) == 1:
                r.append(i)
        return sum(r)

nums = [1,2,3,2]
solution = Solution()
print(solution.sumOfUnique(nums))
