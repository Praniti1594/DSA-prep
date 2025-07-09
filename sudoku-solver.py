# https://leetcode.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows= [set() for _ in range(9)]
        cols= [set() for _ in range(9)]
        boxes= [set() for _ in range(9)]
        empty=[]

        for i in range(9):
            for j in range(9):
                val= board[i][j]
                if val==".":
                    empty.append((i,j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3)*3 + (j//3)].add(val) 

        
        def get_options(i,j):
            box_id= (i//3)*3 + (j//3)
            return {'1', '2', '3', '4', '5', '6','7','8','9'}- rows[i] - cols[j]-boxes[box_id]

        def backtrack():
            if not empty:
                return True

            empty.sort(key=lambda x: get_options(x[0],x[1]))
            i,j= empty.pop(0)

            box_id= (i//3)*3 + (j//3)
            for c in get_options(i,j):
                board[i][j]=c
                rows[i].add(c)
                cols[j].add(c)
                boxes[box_id].add(c)

                if backtrack():
                    return True

                board[i][j]='.'
                rows[i].remove(c)
                cols[j].remove(c)
                boxes[box_id].remove(c)

            empty.insert(0,(i,j))
            return False
        backtrack()


        
        
