class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def dfs(open_count, close_count):

            if len(sol) == 2 * n:
                res.append("".join(sol))
                return

            if open_count < n:
                sol.append("(")
                dfs(open_count + 1, close_count)
                sol.pop()

            if close_count < open_count:
                sol.append(")")
                dfs(open_count, close_count + 1)
                sol.pop()

        dfs(0, 0)

        return res