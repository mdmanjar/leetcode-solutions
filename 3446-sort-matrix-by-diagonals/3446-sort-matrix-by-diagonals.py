class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        arr = [[] for _ in range(2 * n)]

        for i in range(n):
            for j in range(n):
                arr[n + i - j].append(grid[i][j])

        for i in range(2 * n):
            if i < n:
                arr[i].sort(reverse=True)
            else:
                arr[i].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = arr[n + i - j].pop()

        return grid