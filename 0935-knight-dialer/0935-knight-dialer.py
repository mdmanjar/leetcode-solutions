class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        dp = [1] * 10

        for _ in range(2, n + 1):
            new_dp = [0] * 10
            for j in range(10):
                for nxt in jumps[j]:
                    new_dp[j] = (new_dp[j] + dp[nxt]) % MOD
            dp = new_dp

        return sum(dp) % MOD