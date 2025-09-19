from collections import defaultdict
class Spreadsheet:

    def __init__(self, rows: int):
        self.spreed = [defaultdict(int) for i in range(26)]
        
    def setCell(self, cell: str, value: int) -> None:
        pos = ord(cell[0]) - ord('A')
        
        row = int(cell[1:])
        
        self.spreed[pos][row] = value

    def resetCell(self, cell: str) -> None:
        pos = ord(cell[0]) - ord('A')
        
        row = int(cell[1:])
        
        self.spreed[pos][row] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        cell1, cell2 = formula.split('+')
        left = 0
        right = 0
        if cell1[0].isdigit():
            left = int(cell1)
        else:
            left = self.spreed[ord(cell1[0]) - ord('A')][int(cell1[1:])]
        
        
        if cell2[0].isdigit():
            right = int(cell2)
        else:
            right = self.spreed[ord(cell2[0]) - ord('A')][int(cell2[1:])]
            
        return left + right 
            
 
            
        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)