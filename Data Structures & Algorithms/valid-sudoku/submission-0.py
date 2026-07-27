class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = {}
            for j in i:
                if j!=".":
                    row[j] = row.get(j,0)+1
            for k in row.values():
                if k>1:
                    return False
        
        col_ori = []
        for z in range(9):
            col = []
            for x in range(9):
                col.append(board[x][z])
            col_ori.append(col)
        
        for p in col_ori:
            column = {}
            for q in p:
                if q!=".":
                    column[q] = column.get(q,0)+1
            for r in column.values():
                if r>1:
                    return False
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box = {}
                for c in range(box_row,box_row+3):
                    for d in range(box_col,box_col+3):
                        if board[c][d] != ".":
                            box[board[c][d]] = box.get(board[c][d],0)+1
                for v in box.values():
                    if v>1:
                        return False
        return True
