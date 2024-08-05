class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subArrays = []
        n = len(nums)
        for i in range(n):
            subSum = 0
            for j in range(i, n):
                subSum += nums[j]
                subArrays.append(subSum)
        subArrays.sort()
        rangeSum = 0
        for i in range(left-1, right):
            rangeSum = (rangeSum + subArrays[i]) % MOD
        return rangeSum