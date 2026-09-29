
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        rows_sum=[0]*m
        cols_sum=[0]*n
        for i in range(m):
            for j in range(n):
                rows_sum[i]+=grid[i][j]
                cols_sum[j]+=grid[i][j]

        total_sum=sum(rows_sum)

        prefix_sum=0

        for i in range(m):
            prefix_sum+=rows_sum[i]
            if total_sum-prefix_sum==prefix_sum:return True
        prefix_sum=0
        total_sum=sum(cols_sum)

        for i in range(n):
            prefix_sum+=cols_sum[i]
            if total_sum-prefix_sum==prefix_sum:
                return True
        return False