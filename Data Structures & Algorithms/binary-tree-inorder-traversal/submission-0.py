# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        re=[]
        def d(root):
            if not root:
                return
            d(root.left)
            re.append(root.val)
            d(root.right)
        d(root)
        return re