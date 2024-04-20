class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        rows, cols = len(land), len(land[0])
        for r in range(rows):
            for c in range(cols):
                if land[r][c] and (r == 0 or land[r-1][c] == 0) and (c == 0 or land[r][c-1] == 0):
                    nc = c + 1
                    while nc < cols and land[r][nc] == 1:
                        nc += 1
                    nc -= 1
                    nr = r + 1
                    while nr < rows and land[nr][c] == 1:
                        nr += 1
                    nr -= 1
                    ans.append([r, c, nr, nc])
        return ans
