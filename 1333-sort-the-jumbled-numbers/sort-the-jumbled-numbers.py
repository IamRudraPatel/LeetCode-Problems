class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = {}
        for i, num in enumerate(nums):
            newNum = "".join(str(mapping[int(digit)]) for digit in str(num))
            mappedNums[num] = [int(newNum), i]
        nums.sort(key=lambda x: (mappedNums[x][0], mappedNums[x][1]))
        return nums
        