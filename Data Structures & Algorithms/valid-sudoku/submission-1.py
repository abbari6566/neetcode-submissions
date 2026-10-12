class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #validate rows
        for row in range(9):
            validRow = set()
            for col in range(9):
                item = board[row][col]
                if item in validRow:
                    return False
                elif item != '.':
                    validRow.add(item)

        #validate cols
        for row in range(9):
            validCol = set()
            for col in range(9):
                item = board[col][row]
                if item in validCol:
                    return False
                elif item != '.':
                    validCol.add(item)

        #validate 3x3
        starts = [
                    (0,0),(0,3),(0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)
                ]
        for i,j in starts:
            validSubs = set()
            for row in range(i,i+3) :
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in validSubs:
                        return False
                    elif item != '.':
                        validSubs.add(item)
        return True

        