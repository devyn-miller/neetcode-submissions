# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, max_val):
            if not node:
                return 0
            re = 1 if node.val>=max_val else 0
            cur = max(node.val,max_val)
            re += dfs(node.left,cur)
            re += dfs(node.right,cur)
            return re
        return dfs(root,root.val)