print("countBalls")

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        r = 0
        d = {}
        for i in range(lowLimit,highLimit+1):
            a = 0
            si = str(i)
            if len(si) == 1:
                a = i
            else:
                for j in range(0,len(si)):
                    a += int(si[j])
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        return max(d.values())

solution = Solution()
print(solution.countBalls(5, 15))