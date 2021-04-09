print("balancedStringSplit")

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        for v in range(len(s)):
            print(v,s[v])
        return num

s ="RLRRLLRLRL"
solution = Solution()
print(solution.balancedStringSplit(s))