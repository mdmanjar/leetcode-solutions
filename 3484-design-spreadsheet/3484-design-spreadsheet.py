class Spreadsheet:

    def __init__(self, rows: int):
        self.mp={}
        

    def setCell(self, cell: str, value: int) -> None:
        self.mp[cell]=value


    def resetCell(self, cell: str) -> None:
        del self.mp[cell]


    def getValue(self, formula: str) -> int:
        i=formula.index('+')
        def compute(x):
            return self.mp.get(x,0) if x[0] >'9' else int(x) 
        return compute((formula[1:i]))+compute(formula[i+1:])