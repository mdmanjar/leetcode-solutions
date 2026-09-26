class FrontMiddleBackQueue:

    def __init__(self):
        self.left=deque()
        self.right=deque()
    
    def __balanced(self):
        if len(self.left)<len(self.right):
            self.left.append(self.right.popleft())
        if len(self.left)>len(self.right)+1:
            self.right.appendleft(self.left.pop())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.__balanced()
        

    def pushMiddle(self, val: int) -> None:
        if len(self.left)>len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self.__balanced()
        
    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.__balanced()
        

    def popFront(self) -> int:
        if not self.left:return -1
        v=self.left.popleft()
        self.__balanced()
        return v
        

    def popMiddle(self) -> int:
        self.__balanced()
        if not self.left:return -1
        v=self.left.pop()
        self.__balanced()
        return v
        

    def popBack(self) -> int:
        if self.right :
            v=self.right.pop()
            self.__balanced()
            return v
        if self.left:
            v=self.left.pop()
            self.__balanced()
            return v
        return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()