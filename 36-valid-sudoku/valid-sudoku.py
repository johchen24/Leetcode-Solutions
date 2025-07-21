class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        
        count = 0
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                count += 1
                if item == ".":
                    continue
                if (item in rows[i] or item in cols[j] or item in grids[((i // 3) * 3 + j // 3)]):
                    return False
                rows[i].add(item)
                cols[j].add(item)
                grids[((i // 3) * 3 + j // 3)].add(item)
        return True