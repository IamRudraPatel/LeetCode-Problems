class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0

        def checkMagic(r, c):
            # 1-9 Check
            eles = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if (grid[i][j] in eles) or (not 1 <= grid[i][j] <= 9): 
                        return 0
                    eles.add(grid[i][j])
            # Rows Sum
            for i in range(r, r+3):
                if (grid[r][c] + grid[r][c+1] + grid[r][c+2]) != 15: return 0
            # Column Sum
            for i in range(c, c+3):
                if (grid[r][c] + grid[r+1][c] + grid[r+2][c]) != 15: return 0
            # Diagonal Sum
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15) or (
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15
            ): return 0
            return 1

        for r in range(ROWS-2):
            for c in range(COLS-2):
                ans += checkMagic(r, c)
        return ans