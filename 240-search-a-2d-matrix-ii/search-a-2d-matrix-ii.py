class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows, cols = len(matrix), len(matrix[0])

        # leftR, leftC, rightR, rightC = 0, 0, rows - 1, cols - 1
        # while left <= right:
        #     midR, midC = (left + right) // 2
        #     curR, curC = mid // cols, mid % cols

        #     if matrix[curR][curC] < target:
        #         left = mid + 1
        #     elif matrix[curR][curC] > target:
        #         right = mid - 1
        #     else:
        #         return True
        # return False
        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1

        return False