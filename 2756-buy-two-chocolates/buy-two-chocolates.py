class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        summ = prices[0]+prices[1]
        return money if summ > money else money - summ
    