class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop

        heap = []

        for i in nums:
            heappush(heap,i)
            if len(heap) > k:
                heappop(heap)

        return heap[0]