from typing import List
print("minOperations")

class Solution:
    def minOperations(self, nums:List[int]) -> int:
        ans = 0
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                diff = nums[i-1] - nums[i] + 1
                nums[i] = nums[i] + diff
                ans += diff
        return ans

nums =[1,5,2,4,1]
solution = Solution()
print(solution.minOperations(nums))