class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:

        def length(a,b):
            sz=1
            while a!=b:
                if a>b:a>>=1
                else:b>>=1
                sz+=1
            return sz
        return [length(a,b) for a,b in queries]