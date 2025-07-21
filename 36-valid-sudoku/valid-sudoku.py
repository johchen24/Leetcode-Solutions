class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        
        count = 0
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue

                g = (i // 3) * 3 + j // 3
                if (item in rows[i] or item in cols[j] or item in grids[g]):
                    return False
                rows[i].add(item)
                cols[j].add(item)
                grids[g].add(item)
        return True