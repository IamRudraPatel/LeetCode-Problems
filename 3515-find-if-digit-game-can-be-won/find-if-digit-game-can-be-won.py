class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sinDi = 0
        douDi = 0
        for num in nums:
            if num//10 == 0:
                sinDi += num
            else: douDi += num
        return not sinDi == douDi