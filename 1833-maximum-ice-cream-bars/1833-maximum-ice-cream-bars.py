class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        ans=0

        for e in costs:
            if coins>=e:
                coins-=e
                ans+=1
            else:break
        return ans
        