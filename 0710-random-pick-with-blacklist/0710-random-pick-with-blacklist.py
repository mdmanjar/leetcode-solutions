class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = {}
        self.size = n - len(blacklist)

        black = set(blacklist)
        last = n - 1

        for b in blacklist:
            if b < self.size:

                while last in black:
                    last -= 1

                self.map[b] = last
                last -= 1

    def pick(self) -> int:
        x = random.randrange(self.size)
        return self.map.get(x, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()