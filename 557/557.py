print("reverseWords")

class Solution:
    def reverseWords(self, s: str) -> str:
        r = ""
        for v in s.split():
            for i in range(len(v)-1,-1,-1):
                r += v[i]
            r += " "
        return r.strip(" ")

solution = Solution()
print( solution.reverseWords("Let's take LeetCode contest"))