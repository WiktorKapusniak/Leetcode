from typing import List


class Solution:
    def helper(self, matrix, output):
        for i in range(len(matrix)):             
            if i == 0:
                output += matrix[i] 
            elif i == len(matrix) - 1:
                output += reversed(matrix[i]) 
            else: 
                output.append(matrix[i][-1])
                matrix[i].pop(-1)
        if len(matrix)>3:
            for i in range(len(matrix)-2,1,-1):
                if len(matrix[i]) > 0:
                    output.append(matrix[i][0])
                    matrix[i].pop(0)
        matrix = [row for row in matrix if row]
        return matrix[1:-1]
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        while len(matrix)>0:
            matrix = self.helper(matrix, output)
        return output
    
sol = Solution()
print(sol.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
                