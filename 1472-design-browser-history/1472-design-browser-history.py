
class BrowserHistory:

    def __init__(self, homepage: str):
        self.left=[homepage]
        self.right=[]

    def visit(self, url: str) -> None:
        self.left.append(url)
        self.right=[]
        

    def back(self, steps: int) -> str:
        while len(self.left)>1 and steps:
            self.right.append(self.left.pop())
            steps-=1
        return self.left[-1]
        
    def forward(self, steps: int) -> str:
        while self.right and steps:
            self.left.append(self.right.pop())
            steps-=1
        return self.left[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)