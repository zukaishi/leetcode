print("hammingDistance")

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x^y)).count("1")

solution = Solution()
print(solution.hammingDistance(93, 73))
