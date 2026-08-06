class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        lmin = len(self.minHeap)
        lmax = len(self.maxHeap)
        if lmin == lmax:
            if lmin == 0 or num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush_max(self.maxHeap, num)
        elif lmin > lmax:
            if num > self.minHeap[0]:
                temp = heapq.heappushpop(self.minHeap, num)
                heapq.heappush_max(self.maxHeap, temp)
            else:
                heapq.heappush_max(self.maxHeap, num)
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                temp = heapq.heappushpop_max(self.maxHeap, num)
                heapq.heappush(self.minHeap, temp)


        

    def findMedian(self) -> float:
        lmin = len(self.minHeap)
        lmax = len(self.maxHeap)
        if lmin == lmax:
            return (self.minHeap[0] + self.maxHeap[0])/2
        elif lmin > lmax:
            return self.minHeap[0]
        else:
            return self.maxHeap[0]
        
        