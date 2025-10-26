class Bank:
    def __init__(self, balance: list[int]):
        # store 0-indexed internally
        self.bal = balance

    def _valid(self, acc: int) -> bool:
        return 1 <= acc <= len(self.bal)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._valid(account1) and self._valid(account2)):
            return False
        i, j = account1 - 1, account2 - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        self.bal[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        i = account - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        return True
