# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        re=[]
        def t(root):
            if not root:
                return
            re.append(root.val)
            t(root.left)
            t(root.right)
        t(root)
        return re
        