# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def maxheight(root):
            if not root:
                return 0
            return 1 + max(maxheight(root.left), maxheight(root.right))
        def dfs(root):
            if not root:
                return 0
            l = maxheight(root.left)
            r = maxheight(root.right)
            return max(l + r, dfs(root.left), dfs(root.right))
        return dfs(root)
        
            