class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
    
    def balanced(self):
        if len(self.left)+1<len(self.right):
            heapq.heappush_max(self.left,heapq.heappop(self.right))
        elif len(self.left)>len(self.right)+1:
            heapq.heappush(self.right,heapq.heappop_max(self.left))

    def addNum(self, num: int) -> None:

        if self.left and self.left[0]>=num:
            heapq.heappush_max(self.left,num)
        else:
            heapq.heappush(self.right,num)

        self.balanced()
    
    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (self.left[0]+self.right[0])/2
        elif len(self.left)>len(self.right):
            return self.left[0]
        return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()