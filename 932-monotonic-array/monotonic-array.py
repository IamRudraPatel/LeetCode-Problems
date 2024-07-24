class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        for i in range(len(nums)-1):
            # not monotone incresing
            # nums[i] > nums[i+1]
            if not (nums[i] <= nums[i+1]):
                inc = False
                continue
            # not monotone decreasing
            # nums[i] < nums[i+1]
            if not (nums[i] >= nums[i+1]):
                dec = False
        return inc or dec