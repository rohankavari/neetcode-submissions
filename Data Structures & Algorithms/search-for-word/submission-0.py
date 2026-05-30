class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def getNeigh(i, j):
            n = []

            if i != 0:
                n.append([i - 1, j])  # UP

            if j != 0:
                n.append([i, j - 1])  # LEFT

            if i != len(board) - 1:
                n.append([i + 1, j])  # DOWN

            if j != len(board[0]) - 1:
                n.append([i, j + 1])  # RIGHT

            return n

        def dfs(level, i, j, visited):
            if board[i][j] != word[level]:
                return False

            if level == len(word) - 1:
                return True

            N = getNeigh(i, j)

            for neigh in N:
                if neigh not in visited:
                    visited.append([neigh[0], neigh[1]])

                    if dfs(level + 1, neigh[0], neigh[1], visited):
                        return True

                    visited.pop()

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j, [[i, j]]):
                    return True

        return False