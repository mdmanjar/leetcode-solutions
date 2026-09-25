class TextEditor:

    def __init__(self):
        self.left=[]
        self.right=[]
        

    def addText(self, text: str) -> None:
        self.left.extend(text)
        
    def deleteText(self, k: int) -> int:
        k=min(len(self.left),k)
        self.left[-k:]=[]
        return k
    def cursorLeft(self, k: int) -> str:
        k=min(len(self.left),k)
        while k:
            self.right.append(self.left.pop())
            k-=1
        return ''.join(self.left[-10:])
        
    def cursorRight(self, k: int) -> str:
        k=min(len(self.right),k)
        while k:
            self.left.append(self.right.pop())
            k-=1
        return ''.join(self.left[-10:])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)