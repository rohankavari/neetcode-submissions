class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        l = []
        l.append(1)
        l.append(2)

        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
        
        return l[-1]

