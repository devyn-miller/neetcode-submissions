class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        w1, w2 = -1, -1
        res = float('inf')
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] == word1:
                if w2!=-1:
                    res = min(res, i - w2)
                w1 = i
            elif self.wordsDict[i] == word2:
                if w1!=-1:
                    res = min(res, i - w1)
                w2 = i
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
