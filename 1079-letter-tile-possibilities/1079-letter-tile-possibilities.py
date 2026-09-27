
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        arr = list(tiles)
        return self.permute(0, arr)

    def permute(self, start, arr):
        if start == len(arr):
            return 0

        ans = 0

        for i in range(start, len(arr)):
            if not self.isPermutedBefore(start, i - 1, arr[i], arr):
                arr[start], arr[i] = arr[i], arr[start]

                ans += 1 + self.permute(start + 1, arr)

                arr[start], arr[i] = arr[i], arr[start]

        return ans

    def isPermutedBefore(self, i, j, ch, arr):
        while i <= j:
            if arr[i] == ch:
                return True
            i += 1

        return False