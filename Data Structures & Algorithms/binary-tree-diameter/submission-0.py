class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def height(node):
            nonlocal res

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            res = max(res, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return res