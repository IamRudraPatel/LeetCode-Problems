class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m):
            mini, col = mat[i][0], 0
            for j in range(1, n):
                if mat[i][j] < mini:
                    mini = mat[i][j]
                    col = j
            for row in range(m):
                if mini < mat[row][col]:
                    break
            else: ans.append(mini)
        return ans