class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums=["1","2","3","4","5","6","7","8","9"]
        dups=[];
        row_check = False
        column_check=False
        column_check=False

        #checking the row
        for i in range (9):
            for j in range (9):
                if board[i][j]==".":
                    continue
                elif board[i][j] not in dups:
                    dups.append(board[i][j])
                    row_check=True
                else:
                    row_check=False
        
        dups.clear()
        #checking column
        for i in range(9):
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] not in dups:
                    dups.append(board[j][i])
                    column_check=True
                else:
                    column_check=False
        dups.clear()
        for i in range(0,9,3):
            for j in range(3):
                if board[i][j] and board[i+1][j] and board[i+1][j] not in dups:
                    dups.append(board[i][j])
                    dups.append(board[i+1][j])
                    dups.append(board[i+2][j])
                    square_check=True
                elif board[i][j]==".":
                    continue
                elif board[i+1][j]==".":
                    continue
                elif board[i+2][j]==".":
                    continue 
                else:
                    square_check=False

        return (square_check and row_check and column_check)   

