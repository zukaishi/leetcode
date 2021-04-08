print("numIdenticalPairs")

class Solution:
    def numIdenticalPairs(self, nums) -> int:
        num = 0
        nums2 = set(nums)
        for i in nums2:
            count = nums.count(i)
            if count > 1:
                for j in range(count):
                    num += j
                
        return num

int_list = [1,1,1,1]
s = Solution()
test = s.numIdenticalPairs(int_list)
print(test)