# Cracking Faang
"""
Here when we are going up we will decrement the row and increment the column 
    when going up we may have to reset the pointer for 2 cases 
        - case 1 for going up
        +-------+-------+-------+
        |   1   |   2   |   3   |
        +-------+-------+-------+
        |   4   |   5   |   6   |
        +-------+-------+-------+
        |   7   |   8   |   9   |
        +-------+-------+-------+
        when we are 3, and after adding 3 to result our row will be -1 and col will 3, but we have to get back 6 for next processing 
        therefore we should reduce col by 1 and inc row by 2 when curr_col == cols

        when we are at 1, after adding 1 to result our row will be -1 and col will be 1, here in this case we only have to adjust
        the row by inc it by 1 

        -case 2 for going down
        when we are at 4, after adding 4 to the result, our col will be -1 and our row will 2, here we only have to adjust the col by inc 1
        when we are at 8, after adding 8 to the result, our row will 3 and col will be 0, in this case when curr_row == rows, we should increase col by 2 and dec row by 1

"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        res = []
        
        cur_row = cur_col = 0
        going_up = True
        
        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    
                    cur_row -= 1
                    cur_col += 1
                
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                
                going_up = False
            else:
                while cur_row < rows and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])
                    
                    cur_col -= 1
                    cur_row += 1
                
                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                
                going_up = True
        
        return res

# T = NM
# S = NM for ans else 1