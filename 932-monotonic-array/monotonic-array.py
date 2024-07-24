class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(len(nums)-1):
            # not monotone incresing
            # nums[i] > nums[i+1]
            if not (nums[i] <= nums[i+1]):
                increasing = False
            # not monotone decreasing
            # nums[i] < nums[i+1]
            if not (nums[i] >= nums[i+1]):
                decreasing = False
        return increasing or decreasing