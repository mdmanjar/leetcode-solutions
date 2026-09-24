# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:

        def dfs(root):
            if root is None:return True
            if root.left is None and root.right is None:
                return root.val==1

            left=dfs(root.left)
            right=dfs(root.right)

            if root.val==2:
                return left or right
            return left and right
        return dfs(root)
        