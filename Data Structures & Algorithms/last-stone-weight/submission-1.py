class Solution:
    def lastStoneWeight(self,stones):
        from heapq import heappush, heappop
        heap = []
        for i in stones:
            heappush(heap, -1 * i)

        while len(heap) > 1:
            x = -1 * heappop(heap)
            y = -1 * heappop(heap)

            if x == y:
                continue
            elif x < y:
                r = y - x
            else:
                r = x - y
            heappush(heap, -1 * r)
        
        if len(heap) == 0:
            return 0
        return -1 * heap[0]
