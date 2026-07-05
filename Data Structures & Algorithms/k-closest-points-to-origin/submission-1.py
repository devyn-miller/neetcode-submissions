class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidian(x, y):
            return ((x*x) + (y*y))**(1/2)
        points = [[euclidian(p[0],p[1]), p[0],p[1]] for p in points]
        heapq.heapify(points)
        return [[y,z] for x,y,z in  heapq.nsmallest(k, points)]