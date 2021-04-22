from typing import List
print("diagonalSum")

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = 0
        y = 0
        n = 0
        for i in range(0,len(mat)):
            x_max = len(mat) -1
            for j in range(0,len(mat[i])):
                xx = x_max -x
                n += mat[x][y]
                mat[x][y] = 0
                n += mat[i][xx]
                mat[i][xx] = 0
            x += 1
            y += 1
        return n

mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
#mat = [[5]]
#mat = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
print(solution.diagonalSum(mat))
