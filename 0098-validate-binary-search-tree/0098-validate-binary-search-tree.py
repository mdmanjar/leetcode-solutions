# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(root,min_value,max_value):
            if root is None:return True
            if not (min_value<root.val<max_value):
                return False
            return dfs(root.left,min_value,root.val) and dfs(root.right,root.val,max_value)
        return dfs(root,-inf,inf)
        