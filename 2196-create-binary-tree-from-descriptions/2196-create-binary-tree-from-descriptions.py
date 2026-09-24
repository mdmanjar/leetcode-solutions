# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        mp={}

        for parent,_,_ in descriptions:
            if parent in mp:continue
            mp[parent]=TreeNode(parent)
        
        for parent,child,isLeft in descriptions:
            if isLeft:
                if child in mp:
                    mp[parent].left=mp[child]
                else:
                    mp[parent].left=TreeNode(child)
            else:
                if child in mp:
                    mp[parent].right=mp[child]
                else:
                    mp[parent].right=TreeNode(child)   

        for _,child,_ in descriptions:
            if child in mp:
                del mp[child]

        return next(iter(mp.values()))


        