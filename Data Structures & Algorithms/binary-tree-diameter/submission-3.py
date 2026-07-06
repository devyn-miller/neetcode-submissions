# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return 0
            maxR, maxL = dfs(root.right), dfs(root.left)
            res[0] = max(res[0], maxR + maxL)
            return 1 + max(maxR, maxL)
        dfs(root)
        return res[0]