class solution:
    def solved(self,n):
        ans=[]
        board=[["." for _ in range(n)] for _ in range(n)]
        

        self.nqueens(board,0,n,ans)
        return ans

    def nqueens(self,board,row, n,ans):
        if row ==n:
            ans.append(["".join(r) for r in board])
            return

        for i in range(n):
            if self.isafe(board,row,i,n):
                board[row][i]="Q"
                self.nqueens(board,row+1, n,ans)
                board[row][i]="."
    
    def isafe(self,board,row,col,n):

        #horizontal
        for i in range(n) :
            if board[row][i]=="Q":
                return False

        #vertical
        for i in range(n) :
            if board[i][col]=="Q":
                return False


        #left diagonal
        i,j=row-1,col-1
        while i >=0 and j>=0:
            if  board[i][j]=="Q":
                return False
            i-=1
            j-=1

        #right diagonal
        i,j=row-1,col+1
        while i >=0 and j<n:
            if  board[i][j]=="Q":
                return False
            i-=1
            j+=1


        return True

s=solution()
print(s.solved(4))








