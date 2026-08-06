class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1, w2 = -1, -1
        dis = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                if w2 != -1:
                    dis = min(dis, i - w2)
                w1 = i
            if wordsDict[i] == word2:
                if w1 != -1:
                    dis = min(dis, i - w1)
                w2 = i
        return dis