# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = []
        q.append(root)
        res = []
        while len(q) !=0:
            t = []
            level = len(q)
            for _ in range(level):
                top = q.pop(0)
                print(top.val)
                t.append(top.val)
                if top.left is not None:
                    q.append(top.left)
                if top.right is not None:
                    q.append(top.right)
            res.append(t)
        return res
