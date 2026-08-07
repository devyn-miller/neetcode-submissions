# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di= [0]
        def dfs(root):
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            di[0] = max(di[0], l + r)
            return 1+max(dfs(root.left), dfs(root.right))
        dfs(root)
        return di[0]