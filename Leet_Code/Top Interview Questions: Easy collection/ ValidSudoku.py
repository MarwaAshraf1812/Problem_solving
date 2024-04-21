class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict_sudoku = {}
        for i in range(0,9):
            dict_sudoku = {}
            for j in range(0,9):
                if board[i][j] != '.':
                    if board[i][j] not in dict_sudoku:
                        dict_sudoku[board[i][j]] = [(i,j)]
                    else:
                        dict_sudoku[board[i][j]].append((i,j))
                        return False
        for i in range(0,9):
            dict_sudoku = {}
            for j in range(0,9):
                if board[j][i] != '.':
                    if board[j][i] not in dict_sudoku:
                        dict_sudoku[board[j][i]] = [(j,i)]
                    else:
                        dict_sudoku[board[j][i]].append((j,i))
                        return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                dict_sudoku = {}
                for k in range(0,3):
                    for l in range(0,3):
                        if board[i+k][j+l] != '.':
                            if board[i+k][j+l] not in dict_sudoku:
                                dict_sudoku[board[i+k][j+l]] = [(i+k,j+l)]
                            else:
                                dict_sudoku[board[i+k][j+l]].append((i+k,j+l))
                                return False
        return True
                    
"""
507 / 507 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 11.7 MB
"""