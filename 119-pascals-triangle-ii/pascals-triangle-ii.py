class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            nextRow = [0] * (len(ans) + 1)
            for j in range(len(ans)):
                nextRow[j] += ans[j]
                nextRow[j+1] += ans[j]
            ans = nextRow
        return ans