class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameMap = {}
        for i in range(len(heights)):
            nameMap[heights[i]] = i
        ans = []
        for height in sorted(heights, reverse=True):
            ans.append(names[nameMap[height]])
        return ans