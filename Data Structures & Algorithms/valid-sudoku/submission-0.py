class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''
        each dict is a key value pair of the key Nth row/col/sq
        with Value as set of numbers found

        eg)
        rows = {
           0: {2,4,5},
           1: {5, 6, 0},
           ...
           8: {3,4,2,1}
        }
        '''

        rows = {}
        cols = {}
        squares = {}

        def getSquareId(x, y):
            '''
            in a sudoku grid, square numbering goes
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
            '''
            return ( x // 3 ) + 3*(y // 3)


        for x in range(len(board)):
            if x not in rows:
                rows[x] = set()
            for y in range(len(board[x])):
                if y not in cols:
                    cols[y] = set()

                sq = getSquareId(x,y)
                if sq not in squares:
                    squares[sq] = set()
                

                if board[x][y] == ".":
                    # cell empty
                    continue
                
                num = int(board[x][y])
                if num in cols[y]:
                    return False
                else:
                    cols[y].add(num)
                
                if num in rows[x]:
                    return False 
                else:
                    rows[x].add(num)
                
                if num in squares[sq]:
                    return False
                else:
                    squares[sq].add(num)
                
        return True


        