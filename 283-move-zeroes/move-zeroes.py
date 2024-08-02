class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans = [0]*len(nums)
        i = 0
        for num in nums:
            if num!=0:
                ans[i] = num
                i += 1
        for i in range(len(nums)):
            nums[i] = ans[i]
        