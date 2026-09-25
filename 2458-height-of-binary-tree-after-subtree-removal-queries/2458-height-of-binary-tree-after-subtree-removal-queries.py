# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        mp=defaultdict(lambda:-inf)

        def _left_(root,depth):
            nonlocal max_depth
            if root is None:return
            mp[root.val]=max_depth
            max_depth=max(max_depth,depth)
            _left_(root.left,depth+1)
            _left_(root.right,depth+1)
        
        def _right_(root,depth):
            nonlocal max_depth
            if root is None:return
            mp[root.val]=max(mp.get(root.val,0),max_depth)
            max_depth=max(max_depth,depth)
            _right_(root.right,depth+1)
            _right_(root.left,depth+1)

        max_depth=0
        _left_(root,0)
        max_depth=0
        _right_(root,0)
        return [mp[i] for i in queries]
            

        