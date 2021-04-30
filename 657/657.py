print("judgeCircle")

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = False
        x = y = 0
        for v in moves:
            if v == "U":
                y -= 1
            elif v == "D":
                y += 1
            elif v == "L":
                x -= 1
            elif v == "R":
                x += 1
        if x == 0 and y == 0:
            r = True
        return r

solution = Solution()
print(solution.judgeCircle("LL"))