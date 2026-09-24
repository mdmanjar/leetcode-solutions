class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:return root
        q=deque([root])
        level=0

        while q:
            nodes=list(q)
            if level&1:
                left=0
                right=len(nodes)-1
                while left<right:
                    nodes[left].val,nodes[right].val=nodes[right].val,nodes[left].val
                    left+=1
                    right-=1

            for _ in range(len(q)):
                cur=q.popleft()
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)
            level=~level

        return root