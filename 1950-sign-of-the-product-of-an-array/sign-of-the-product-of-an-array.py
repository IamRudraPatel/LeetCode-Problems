class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zero = 0
        neg = 0
        for num in nums:
            if num==0: zero+=1
            elif num < 0: neg += 1
        if zero: return 0
        return 1 if neg%2==0 else -1