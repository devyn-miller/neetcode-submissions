# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            r, num = q.popleft()
            if r:
                res[num].append(r.val)
                q.append((r.left, num - 1))
                q.append((r.right, num + 1))
        ret = [[key, value] for key, value in res.items()]
        ret.sort(key=lambda x: x[0])
        return list(value for key, value in ret)