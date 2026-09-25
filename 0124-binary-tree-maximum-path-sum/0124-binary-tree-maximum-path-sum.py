class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            ans = max(ans, left + right + node.val)

            return max(left, right) + node.val

        dfs(root)

        return ans