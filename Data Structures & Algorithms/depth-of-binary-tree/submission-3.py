# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = []
        stack.append((root,1))
        res = 0
        while len(stack)!=0:
            top,depth = stack.pop()
            if top.right is not None:
                stack.append((top.right,depth+1))
            if top.left is not None:
                stack.append((top.left,depth+1))
            
            if top.right is None and top.left is None:
                res = max(depth,res)

        return res