class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
       # Check for rows
        for i in board:
            for j in i:
                if j !="." and i.count(j)>1:
                    return False

       # Check for columns
        for j in range(9):
            li=[]
            li.append(board[0][j])
            li.append(board[1][j])
            li.append(board[2][j])
            li.append(board[3][j])
            li.append(board[4][j])
            li.append(board[5][j])
            li.append(board[6][j])
            li.append(board[7][j])
            li.append(board[8][j])
            for i in li:
                if i!="." and li.count(i) >1:
                    return False
       # Check into 3X3 submatrix 
        i=0
        while i<=6:
            j=i+1
            k=i+2
            m=0
            n=3
            while n<=9:
                lis=[]
                por=[]
                lis.append(board[i][m:n])
                lis.append(board[j][m:n])
                lis.append(board[k][m:n])
                #return lis
                for z in lis:
                    por.append(z[0])
                    por.append(z[1])
                    por.append(z[2])
                for _ in por:
                    if _!="." and por.count(_)>1:
                        return False
                    
                m+=3
                n+=3
            i=i+3
        else:
            return True