class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        sol = []

        def valid(r, c, placed):
            if c in placed["col"]:
                return False

            if r - c in placed["diag1"]:
                return False

            if r + c in placed["diag2"]:
                return False

            return True

        def dfs(r, placed):
            if r == n:
                board = []

                for col in sol:
                    row = ["."] * n
                    row[col] = "Q"
                    board.append("".join(row))

                res.append(board)
                return

            for c in range(n):
                if valid(r, c, placed):

                    # place queen
                    sol.append(c)
                    placed["col"].append(c)
                    placed["diag1"].append(r - c)
                    placed["diag2"].append(r + c)

                    dfs(r + 1, placed)

                    # backtrack
                    sol.pop()
                    placed["col"].pop()
                    placed["diag1"].pop()
                    placed["diag2"].pop()

        dfs(
            0,
            {
                "col": [],
                "diag1": [],
                "diag2": [],
            },
        )

        return res