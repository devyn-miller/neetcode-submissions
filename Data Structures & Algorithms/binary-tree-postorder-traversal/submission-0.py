# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        re=[]
        def l(root):
            if not root:
                return
            l(root.left)
            l(root.right)
            re.append(root.val)
        l(root)
        return re
