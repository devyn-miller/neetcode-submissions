class HitCounter:

    def __init__(self):
        self.q = deque()
        

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        i=0
        while i < len(self.q):
            if timestamp - self.q[i] >= 300:
                self.q.popleft()
            else:
                break
            

        

    def getHits(self, timestamp: int) -> int:
        i=0
        while i < len(self.q):
            if timestamp - self.q[i] >= 300:
                self.q.popleft()
            else:
                break
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
