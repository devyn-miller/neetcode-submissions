# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append([root])
        while q:
            temp_res = []
            temp_append = []
            n = q.popleft()
            len_n = len(n)
            for i in range(len_n):
                temp_res.append(n[i].val)
                if n[i].left:
                    temp_append.append(n[i].left)
                if n[i].right:
                    temp_append.append(n[i].right)
            if temp_res:
                res.append(temp_res)
            if temp_append:
                q.append(temp_append)
        return res

