# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(smallest, node, biggest):
            if not node:
                return True
            if not (smallest < node.val < biggest):
                return False
            return dfs(smallest, node.left, node.val) and dfs(node.val, node.right, biggest)

        return dfs(-1001, root, 1001)
