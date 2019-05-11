class Solution:
    def isValidSudoku(self, board) -> bool:
        row = []
        col = []
        box = []
        for i in range(9):
            row.append({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0})
            col.append({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0})
            box.append({'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0})

        for i in range(9):
            for j in range(9):
                if row[i][board[i][j]] == 1 and board[i][j] != '.':
                    return False
                else:
                    row[i][board[i][j]] = 1

                if col[j][board[i][j]] == 1 and board[i][j] != '.':
                    return False
                else:
                    col[j][board[i][j]] = 1

                boxIndex = i // 3 * 3 + j // 3
                if box[boxIndex][board[i][j]] == 1 and board[i][j] != '.':
                    return False
                else:
                    box[boxIndex][board[i][j]] = 1

        return True

s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))