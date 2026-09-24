# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans=0
        level=-1

        def dfs(root,l):
            nonlocal ans,level
            if root is None:
                return
            
            if level<l:
                level=l
                ans=root.val
            dfs(root.left,l+1)
            dfs(root.right,l+1)
        dfs(root,0)
        return ans
        


        