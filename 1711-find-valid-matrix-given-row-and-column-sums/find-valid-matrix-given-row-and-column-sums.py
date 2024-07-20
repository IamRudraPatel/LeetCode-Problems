class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)
        ans = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            ans[r][0] = rowSum[r]
        for c in range(COLS):
            curColSum = 0
            for r in range(ROWS):
                curColSum += ans[r][c]
            r = 0
            while curColSum > colSum[c]:
                diff = curColSum - colSum[c]
                maxShift = min(ans[r][c], diff)
                ans[r][c] -= maxShift
                ans[r][c+1] += maxShift
                curColSum -= maxShift
                r += 1
        return ans