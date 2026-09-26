from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def balance(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)

    def pushBack(self, val):
        self.right.append(val)
        self.balance()

    def popFront(self):
        if not self.left and not self.right:
            return -1

        if self.left:
            ans = self.left.popleft()
        else:
            ans = self.right.popleft()

        self.balance()
        return ans

    def popMiddle(self):
        if not self.left and not self.right:
            return -1

        ans = self.left.pop()
        self.balance()
        return ans

    def popBack(self):
        if not self.left and not self.right:
            return -1

        if self.right:
            ans = self.right.pop()
        else:
            ans = self.left.pop()

        self.balance()
        return ans