class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        q=deque([root])
        ans=0

        while q:
            size=len(q)
            arr=[]

            for i in range(size):
                cur=q.popleft()
                arr.append((cur.val<<18)|i)

                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)

            arr.sort()

            i=0
            while i<size:
                index=arr[i]&((1<<18)-1)
                if index!=i:
                    arr[i],arr[index]=arr[index],arr[i]
                    ans+=1
                else:
                    i+=1

        return ans