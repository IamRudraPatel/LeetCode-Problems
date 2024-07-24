class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = []
        for i, num in enumerate(nums):
            newNum = 0
            base = 1
            if num == 0: newNum = mapping[0]
            else: 
                while num:
                    digit = num % 10
                    num = num // 10
                    newNum += base * mapping[digit]
                    base *= 10
            mappedNums.append((newNum, i)) # (mappedNum, index)
        mappedNums.sort()
        return [nums[pair[1]] for pair in mappedNums]         