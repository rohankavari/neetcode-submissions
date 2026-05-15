class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math

        def dist(b):
            return (0 - b[0]) ** 2 + (0 - b[1]) ** 2

        # res = []
        # for i in points:
        #     d = dist(i)
        #     res.append([i, d])

        ans = sorted(points, key=lambda x: dist(x))
        return ans[:k]
