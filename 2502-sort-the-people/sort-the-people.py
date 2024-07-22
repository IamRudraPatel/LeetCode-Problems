class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameMap = {}
        for i in range(len(heights)):
            nameMap[heights[i]] = names[i]
        ans = []
        for height in sorted(heights, reverse=True):
            ans.append(nameMap[height])
        return ans