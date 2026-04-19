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
        re = [[root.val]]
        q = deque()
        q.append(root)
        while q:
            l=len(q)
            temp = []
            for _ in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                    temp.append(n.left.val)
                if n.right:
                    temp.append(n.right.val)
                    q.append(n.right)
            if temp:
                re.append(temp)
        return re