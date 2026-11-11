class Solution:
    def insert(self, arr: list[list[int]], x: list[int]) -> list[list[int]]:
        ans=[]
        i=0

        while i<len(arr):
            if arr[i][1]>=x[0]:break
            ans.append(arr[i])
            i+=1
        ans.append(x)

        while i<len(arr):
            if ans[-1][1]<arr[i][0]:break
            ans[-1][0]=min(ans[-1][0],arr[i][0])
            ans[-1][1]=max(ans[-1][1],arr[i][1])
            i+=1
        while i<len(arr):
            ans.append(arr[i])
            i+=1
        return ans
        