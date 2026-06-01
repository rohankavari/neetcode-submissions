class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":return []
        numpad = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        a = []
        for n in digits:a.append(numpad[int(n)])

        res,sol= [],[]
        def dfs(level):
            # print(f"Level {level}")
            if level == len(a):
                res.append("".join(sol))
                return
            
            for i in a[level]:
                # print(f"  ADD {i}")
                sol.append(i)
                dfs(level+1)
                sol.pop()
        
        dfs(0)
        return res