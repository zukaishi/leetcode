print("shuffle")

class Solution:
    def shuffle(self, nums, n) -> [int]:
        i = 0
        rlist = []
        for _ in nums:
            rlist = rlist + nums[i:i+1:1]
            rlist = rlist + nums[n+i:n+i+1:1]
            i += 1
            if i >= n:
                break
        return rlist

nums = [2,5,1,3,4,7]
n =3
s = Solution()
test = s.shuffle(nums,n)
print(test)
