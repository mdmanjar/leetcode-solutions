# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans=[]


        def dfs(root,level):
            if root is None:return
            if level==len(ans):
                ans.append([])
            ans[level].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)
        return ans


        