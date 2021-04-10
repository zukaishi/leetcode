print("balancedStringSplit")

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return_num = 0
        start = 0
        for start in range(len(s)):
            for i in range(1,round(len(s)/2)):
                num = i+1
                v = [s[j: j+num] for j in range(start, len(s), num)]
                print(v)
                # for v in range(len(s)):
        return return_num

s ="RLRRLLRLRL"
solution = Solution()
print(solution.balancedStringSplit(s))