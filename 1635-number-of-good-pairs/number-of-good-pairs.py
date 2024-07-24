class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seenEle = {}
        ans = 0
        for i in range(len(nums)):
            seenEle[nums[i]] = seenEle.get(nums[i], 0) + 1
        for freq in seenEle.values():
            ans += (freq*(freq-1))//2
        return ans