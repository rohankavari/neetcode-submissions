class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()
        def dfs(t, start):
            if t == 0:
                res.append(sol.copy())
                return
            if t < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sol.append(candidates[i])
                dfs(t - candidates[i], i+1)
                sol.pop()

        dfs(target, 0)
        return res