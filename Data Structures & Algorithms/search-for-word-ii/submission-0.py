class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        ROW, COL = len(board),len(board[0])
        root = TrieNode()
        for word in words:
            root.insert(word)
        visiting = set()
        res = set()

        def dfs(r,c,node,word):
            if r>=ROW or r<0 or c<0 or c>=COL or (r,c) in visiting or board[r][c] not in node.children:
                return
            visiting.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eow:
                res.add(word)
            for dr,dc in di:
                dfs(r+dr,c+dc,node,word)
            visiting.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                    dfs(r,c,root,"")
        return list(res)
