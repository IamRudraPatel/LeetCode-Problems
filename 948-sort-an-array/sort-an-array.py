class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freq = {}
        maxi, mini = -1, 5 * 10**4 + 1
        for num in nums:
            if num < mini: mini = num
            if num > maxi: maxi = num
            freq[num] = freq.get(num, 0) + 1
        newArr = [0]*len(nums)
        idx = 0
        for num in range(mini, maxi+1):
            occur = freq.get(num, 0)
            for _ in range(occur):
                newArr[idx] = num
                idx += 1
        return newArr 