class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i = 0
        while(i<N):
            if (nums[i]!=nums[nums[i]-1]):
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            else: i+=1
        ans = []
        for i in range(N):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans