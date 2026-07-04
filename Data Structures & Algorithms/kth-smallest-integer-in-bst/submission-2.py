# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [k, 0]
        def helper(root):
            if not root:
                return
            helper(root.left)
            res[0] -= 1
            if res[0] == 0:
                res[1] = root.val
                return
            helper(root.right)
        helper(root)
        return res[1]