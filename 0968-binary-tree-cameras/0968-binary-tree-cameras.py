# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        if not root:return 0
        camera=0

        def dfs(root):
            nonlocal camera
            if not root:return 3

            left=dfs(root.left)
            right=dfs(root.right)
            
            if 1 in (left,right):
                camera+=1
                return 2
            if 2 in (left,right):
                return 3
            return 1


        if dfs(root)==1:
            camera+=1

        return camera



        