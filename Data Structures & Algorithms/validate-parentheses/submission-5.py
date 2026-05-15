class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0 or s[0] in ["]",")","}"] or s[-1] in ["(","{","["]:
            return False
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            else:
                if i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
