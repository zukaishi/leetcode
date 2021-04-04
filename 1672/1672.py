print("maximumWealth")

class Solution:
    def maximumWealth(self, accounts) -> int:
        max = 0
        for v in accounts:
            s = sum(v)
            if s > max:
                max = s
        return max

int_list = [[1,2,3],[3,2,1]]
s = Solution()
test = s.maximumWealth(int_list)
print(test)
