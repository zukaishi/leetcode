https://leetcode.com/problems/range-sum-of-bst/

```pyton
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
```