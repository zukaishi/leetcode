print("shuffle")

class Solution:
    def shuffle(self, nums, s) -> [int]:
        n = 0
        for _ in nums:
            print(nums[n:n+s:1])
            n += s
            if n >= len(nums):
                break

        return_s = [1,2,3]
        return return_s

nums = [2,5,1,3,4,7]
n =3
s = Solution()
test = s.shuffle(nums,n)
print(test)
