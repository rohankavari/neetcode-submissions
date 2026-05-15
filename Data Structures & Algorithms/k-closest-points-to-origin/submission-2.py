class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush , heappop
        def dist(b):
            return (0 - b[0]) ** 2 + (0 - b[1]) ** 2

        heap = []

        for i in points:
            heappush(heap,(dist(i),i))
        
        res = []
        for _ in range(k):
            d, p = heappop(heap)
            res.append(p)
        
        return res