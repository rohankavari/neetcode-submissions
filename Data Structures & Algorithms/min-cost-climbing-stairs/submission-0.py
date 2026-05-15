class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = []
        l.append(cost[0])
        l.append(cost[1])

        for i in range(2,len(cost)):
            c = min(l[i-1],l[i-2]) + cost[i]
            l.append(c)
        print(l)
        return min(l[-1],l[-2])
