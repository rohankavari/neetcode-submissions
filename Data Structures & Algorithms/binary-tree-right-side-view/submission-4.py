# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        d = []
        d.append((root,1))
        r = {}
        while len(d) > 0:
            n,l = d.pop(0)
            if l not in r:
                r[l] = n.val
            if n.right:
                d.append((n.right,l+1))
            if n.left:
                d.append((n.left,l+1))           
        # print([i[0] for i in r.values()])
        print(r.values())
        return list(r.values())