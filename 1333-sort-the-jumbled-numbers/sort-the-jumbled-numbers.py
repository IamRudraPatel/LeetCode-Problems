class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = []
        for i, num in enumerate(nums):
            newNum = 0
            for digit in str(num):
                newNum *= 10
                newNum += mapping[int(digit)]
            mappedNums.append((newNum, i)) # (mappedNum, index)
        mappedNums.sort()
        return [nums[pair[1]] for pair in mappedNums]         