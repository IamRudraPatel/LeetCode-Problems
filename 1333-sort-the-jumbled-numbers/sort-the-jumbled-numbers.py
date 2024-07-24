class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = []
        for i, num in enumerate(nums):
            newNum = 0
            place = 1
            if num == 0: 
                mappedNums.append((mapping[0], i))
                continue
            while num:
                newNum += place * mapping[num % 10]
                num = num // 10
                place *= 10
            mappedNums.append((newNum, i)) # (mappedNum, index)
        mappedNums.sort()
        return [nums[pair[1]] for pair in mappedNums]         