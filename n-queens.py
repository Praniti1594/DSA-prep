# https://leetcode.com/problems/n-queens/
class Solution(object):
    def solveNQueens(self, n):
        def isSafe(row, col, board, n):
            duprow= row
            dupcol= col

            #upper diagonal
            while col>=0 and row>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
                row-=1

            row= duprow
            col=dupcol
            #left rows
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
            
            row=duprow
            col=dupcol
            # lower diagonal
            while row< n and col>=0:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1

            return True

        def solve(col, board, ans, n):
            if col==n:
                ans.append(["".join(board[r])for r in range(n)])
                return

            for row in range(n):
                if isSafe(row, col, board, n):
                    board[row][col]='Q'
                    solve(col+1, board, ans,n)
                    board[row][col]='.'
                
        board= [['.'for _ in range(n)]for _ in range(n)]
        ans=[]
        solve(0,board, ans, n)
        return ans

   
        
