class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = []
        r, c = rStart, cStart
        steps, i = 1, 0
        while (len(ans) < rows * cols):
            for _ in range(2):
                cr, cc = direction[i]
                for __ in range(steps):
                    if (-1 < r < rows and -1 < c < cols):
                        ans.append([r, c])
                    r, c = r + cr, c + cc
                i = (i + 1) % 4
            steps += 1
        return ans