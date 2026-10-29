ans=sorted([k for k ,v in Counter(i**3+j**3 for i in range(1,1001) for j in range(i,1001)).items() if v>=2])

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        return ans[:bisect_right(ans,n)]