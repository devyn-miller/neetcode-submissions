# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ct = k
        self.ans = None
        def inorder(node):
            if not node or self.ans != None:
                return
            inorder(node.left)
            self.ct -=1
            if self.ct==0:
                self.ans =node.val
            inorder(node.right)

        inorder(root)
        return self.ans