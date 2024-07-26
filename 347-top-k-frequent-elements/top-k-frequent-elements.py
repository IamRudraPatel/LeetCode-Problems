class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        countMap = {}
        freq = [[] for i in range(n+1)]
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        for num, count in countMap.items():
            freq[count].append(num)
        ans = []
        for i in range(n, 0, -1):
            if freq[i]!=[]:
                for n in freq[i]:
                    ans.append(n)
                    k -= 1
                    if k == 0: return ans