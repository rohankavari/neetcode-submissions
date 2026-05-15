class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(h, w):
            return h * w

        l = 0
        r = len(heights) - 1
        res = 0

        while r > l :
            res = max(area(min(heights[l],heights[r]),r-l),res)

            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
        return res