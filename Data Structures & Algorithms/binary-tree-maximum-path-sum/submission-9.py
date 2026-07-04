# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def path(root):
            if not root:
                return 0
            lMax, rMax = path(root.left),  path(root.right)
            curr = root.val + max(0, lMax) + max(0, rMax)
            res[0] = max(res[0], curr)
            return root.val + max(0, lMax, rMax)
        path(root)
        return res[0]