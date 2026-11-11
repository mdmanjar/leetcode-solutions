# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        def dfs(root):
            if root is None:return root
            left=root.left
            root.left=dfs(root.right)
            root.right=dfs(left)
            return root
        return dfs(root)
        