class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []


    def addNum(self, num: int) -> None:
        l_min = len(self.minHeap)
        l_max = len(self.maxHeap)
        diff = abs(l_min - l_max)
        if diff == 0:
            if l_min == 0 or num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush_max(self.maxHeap, num)
        elif l_min > l_max:
            if num > self.minHeap[0]:
                temp = heapq.heapreplace(self.minHeap, num)
                heapq.heappush_max(self.maxHeap, temp)
            else:
                heapq.heappush_max(self.maxHeap, num)
        else:
            if num < self.maxHeap[0]:
                temp = heapq.heapreplace_max(self.maxHeap, num)
                heapq.heappush(self.minHeap, temp)
            else:
                heapq.heappush(self.minHeap, num)

        

    def findMedian(self) -> float:
        print(self.minHeap,self.maxHeap)
        l_min = len(self.minHeap)
        l_max = len(self.maxHeap)
        diff = abs(l_min - l_max)
        if diff == 0:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        if l_min > l_max:
            return self.minHeap[0]
        return self.maxHeap[0]
        
        