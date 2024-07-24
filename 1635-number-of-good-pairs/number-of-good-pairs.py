class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seenEle = {}
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if nums[i] in seenEle:
                ans += seenEle[num]
            seenEle[num] = seenEle.get(num, 0) + 1
        return ans