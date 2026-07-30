class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        sh = float('inf')
        curr1_found, curr2_found = False, False
        curr1, curr2 = 0, 0
        for i in range(len(self.d)):
            if word1 == self.d[i]:
                curr1 = i
                curr1_found = True
                if curr2_found:
                    sh = min(sh, i - curr2)

            if word2 == self.d[i]:
                curr2 = i
                curr2_found = True
                if curr1_found:
                    sh = min(sh, i - curr1)
        return sh




        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
