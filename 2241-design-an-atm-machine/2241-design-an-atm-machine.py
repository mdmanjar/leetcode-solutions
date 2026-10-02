class ATM:

    def __init__(self):
        self.notes_count = [0] * 5
        self.coins = (20, 50, 100, 200, 500)

    def deposit(self, notes: list[int]) -> None:
        for i in range(5):
            self.notes_count[i] += notes[i]

    def withdraw(self, amount: int) -> list[int]:
        ans = [0] * 5

        for i in range(4, -1, -1):
            take = min(amount // self.coins[i], self.notes_count[i])
            ans[i] = take
            amount -= take * self.coins[i]

        if amount:
            return [-1]

        for i in range(5):
            self.notes_count[i] -= ans[i]

        return ans
            

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)