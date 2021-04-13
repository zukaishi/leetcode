print("rangeSumBST")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return_num = 0
        for v in root:
            if v >= low and v <= height:
                return_num += v
        return return_num

root = [10,5,15,3,7,null,18]
low = 7
height = 15
solution = Solution()
print(solution.rangeSumBST(root,low,height))