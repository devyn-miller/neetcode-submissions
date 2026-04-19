# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val==q.val:
            return p.val
        if p.val>q.val:
            p,q=q,p
        while root:
            if root.val == p or root.val == q:
                return p
            if p.val<=root.val <= q.val:
                return root
            if root.right and q.val<root.right.val:
                root = root.left
            elif root.left and p.val>root.left.val:
                root = root.right
            else:
                return root
    