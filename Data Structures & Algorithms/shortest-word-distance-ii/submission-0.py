class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        diff = float('inf')
        first, second = -1, -1
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] == word1:
                if second != -1:
                    diff = min(diff, abs(second - i))
                first = i
            elif self.wordsDict[i] == word2:
                if first != -1:
                    diff = min(diff, abs(i - first))
                second = i
        return diff
        
                



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
