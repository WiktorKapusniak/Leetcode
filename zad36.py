from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            uniqueInts = set()
            for line in board:
                before = len(uniqueInts)
                if line[i].isdigit():
                    uniqueInts.add(line[i])
                after = len(uniqueInts)
                if line[i].isdigit() and before==after:
                    return False
        for i in board:
            uniqueInts = set()
            for j in i:
                before = len(uniqueInts)
                if j.isdigit():
                    uniqueInts.add(j)
                after = len(uniqueInts)
                if j.isdigit() and before==after:
                    return False
                
        for i in range(0,9,3):

            for j in range(0,9,3):
                uniqueInts = set()
                for row in range(i,i+3):
                    for column in range(j,j+3):
                        before = len(uniqueInts)
                        if board[row][column].isdigit():
                            uniqueInts.add(board[row][column])
                        after = len(uniqueInts)
                        if board[row][column].isdigit() and before==after:
                            return False
        return True
    

sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
