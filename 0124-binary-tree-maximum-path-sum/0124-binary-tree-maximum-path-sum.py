# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_value=-inf

        def dfs(root):
            nonlocal max_value
            if root is None:return 0
            left=max(dfs(root.left),0)
            right=max(dfs(root.right),0)
            max_value=max(max_value,left+right+root.val)
            return max(0,root.val+max(left,right))
        dfs(root)
        return max_value
        