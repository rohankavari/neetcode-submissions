class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        from heapq import heappush, heappop

        for i in nums:
            heappush(self.heap,i)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        from heapq import heappush, heappop
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        
