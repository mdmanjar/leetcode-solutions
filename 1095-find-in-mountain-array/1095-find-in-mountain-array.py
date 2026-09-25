# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class MountainArray:
    def get(self, index: int) -> int:pass
    def length(self) -> int:pass

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        n=arr.length()
        if n<3:return -1
        def peek():
            left=1
            right=n-2

            while left<=right:
                mid=left+(right-left)//2
                l=arr.get(mid-1)
                r=arr.get(mid+1)
                m=arr.get(mid)
                if l<m>r:
                    return mid
                elif l<m:
                    left=mid+1
                else:
                    right=mid-1
        def left(left,right):
            while left<=right:
                mid=left+(right-left)//2
                m=arr.get(mid)
                if m==target:return mid
                if target<m:
                    right=mid-1
                else:
                    left=mid+1
            return -1

        def right(left,right):
            while left<=right:
                mid=left+(right-left)//2
                m=arr.get(mid)
                if m==target:return mid
                if target<m:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        p=peek()
        l=left(0,p)
        if l!=-1:return l
        return right(p,n-1)
                


        