class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.i = 0

        def dfs(x, i):
            if i >= len(x):
                return

            if x[i].isInteger():
                self.arr.append(x[i].getInteger())
            else:
                dfs(x[i].getList(), 0)

            dfs(x, i + 1)

        dfs(nestedList, 0)

    def next(self) -> int:
        val = self.arr[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.arr)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())