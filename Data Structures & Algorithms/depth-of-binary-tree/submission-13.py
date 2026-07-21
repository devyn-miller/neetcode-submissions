# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack, res = [[root, 1]], 0
        while stack:
            node, level = stack.pop()
            if node.left:
                res = max(res, level + 1)
                stack.append([node.left, 1 + level])
            if node.right:
                res = max(res, level + 1)
                stack.append([node.right, 1 + level])

        return max(1,res)
        