# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def dfs(r):
            if r is None:

                return 
            ans.append(str(r.val))
            if r.left or r.right:
                ans.append('(')
                dfs(r.left)
                ans.append(')')
            if r.right:
                ans.append('(')
                dfs(r.right)
                ans.append(')')
        dfs(root)
        return ''.join(ans)
        