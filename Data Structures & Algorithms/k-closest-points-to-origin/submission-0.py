class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        def dist(b):
            return math.sqrt((0-b[0])**2+(0-b[1])**2)
        
        res = []
        for i in points:
            d = dist(i)
            res.append([i,d])
        
        ans = sorted(res,key = lambda x:x[1])
        return [i[0] for i in ans][:k]