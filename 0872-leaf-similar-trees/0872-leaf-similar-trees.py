# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        leaves=[]

        def dfs(root):
            if not root:return
            if not root.left and not root.right:
                leaves.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root1)

        i=0

        def check(root):
            nonlocal i
            if root is None:return True

            if not root.left and not root.right:
                if i==len(leaves) or leaves[i]!=root.val:
                    return False
                i+=1
                return True

            return check(root.left) and check(root.right)

        return check(root2) and i==len(leaves)
        