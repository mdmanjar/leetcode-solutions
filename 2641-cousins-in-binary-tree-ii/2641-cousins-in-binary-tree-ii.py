# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        arr=[]
        def dfs(root,level):
            if root is None:return
            if level==len(arr):arr.append(0)
            arr[level]+=root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)

        def fill(root,level):
            if root is None:return
            if root.left:
                x=arr[level+1]-root.left.val
                if root.right:
                    x-=root.right.val
                    root.right.val=x
                root.left.val=x
            elif root.right:
                root.right.val=arr[level+1]-root.right.val
            fill(root.left,level+1)
            fill(root.right,level+1)
        root.val=0
        fill(root,0)
        return root
        