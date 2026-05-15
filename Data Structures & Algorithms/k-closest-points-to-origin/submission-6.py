class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush, heappop

        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        heap = []

        for point in points:
            d = -dist(point)

            if len(heap) < k:
                heappush(heap, (d, point))
            else:
                if d > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (d, point))

        return [point for d, point in heap]