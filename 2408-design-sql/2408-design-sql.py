from typing import List, Dict

class SQL:
    class Table:
        def __init__(self, column_size: int):
            self.auto_inc_id = 1  # 1-indexed IDs
            self.column_size = column_size
            self.rows: Dict[int, List[str]] = {}  # Key: row_id, Value: List[str] (columns)

    def __init__(self, names: List[str], columns: List[int]):
        self.tables: Dict[str, SQL.Table] = {names[i]: SQL.Table(columns[i]) for i in range(len(names))}

    def ins(self, name: str, row: List[str]) -> bool:
        table = self.tables.get(name)
        if not table or len(row) != table.column_size:
            return False
        table.rows[table.auto_inc_id] = row
        table.auto_inc_id += 1
        return True

    def rmv(self, name: str, row_id: int) -> None:
        table = self.tables.get(name)
        if table:
            table.rows.pop(row_id, None)  # Safe removal, does nothing if row_id is not present

    def sel(self, name: str, row_id: int, column_id: int) -> str:
        table = self.tables.get(name)
        if not table:
            return "<null>"
        row = table.rows.get(row_id)
        if not row or column_id > len(row):  # column_id is 1-based index
            return "<null>"
        return row[column_id - 1]

    def exp(self, name: str) -> List[str]:
        table = self.tables.get(name)
        if not table:
            return []
        return [f"{row_id},{','.join(row)}" for row_id, row in table.rows.items()]

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)