class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def dfs(t, start):
            if t == 0:
                res.append(sol.copy())
                return
            if t < 0:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                dfs(t - nums[i], i)
                sol.pop()

        dfs(target, 0)
        return res
