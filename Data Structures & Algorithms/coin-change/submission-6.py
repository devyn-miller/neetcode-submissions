class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount + 1] * (amount + 1)
        cache[0] = 0
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - c])
        if cache[amount] == amount + 1:
            return -1
        return cache[amount]
