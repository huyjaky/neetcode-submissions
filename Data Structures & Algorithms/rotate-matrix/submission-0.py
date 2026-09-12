from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Bước 1: Chuyển vị ma trận
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col],
                )

        # Bước 2: Đảo ngược từng hàng
        for row in matrix:
            row.reverse()