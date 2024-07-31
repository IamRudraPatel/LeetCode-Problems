class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        amount, bought = money, 0
        for price in prices:
            if (price <= amount) and (bought!=2):
                amount -= price
                bought += 1
        return amount if bought == 2 else money
