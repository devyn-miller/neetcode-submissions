# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def bst(mi,root,ma):
            if not root:
                return True
            if not (mi < root.val < ma):
                return False
            # if root.left and root.right:
            return bst(root.val,root.right,ma) and bst(mi,root.left,root.val)
            # elif root.right:
            #     return bst(mi,root.right,root.val)
            # else:
            #     return bst(root.val,root.left,ma)
        return bst(-float('inf'),root,float('inf'))