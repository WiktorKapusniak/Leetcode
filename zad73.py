from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        track_of_column = {}
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        track_of_column[j] = '0'
                    matrix[i][j] = 0
        for i in range(len(matrix)):
            for index in track_of_column:
                matrix[i][index] = 0