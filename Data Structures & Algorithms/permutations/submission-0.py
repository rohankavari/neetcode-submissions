class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]
        def dfs(n):
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            for i in n:
                sol.append(i)
                temp = n.copy()
                temp.remove(i)
                dfs(temp)
                sol.pop()
        dfs(nums)
        return res