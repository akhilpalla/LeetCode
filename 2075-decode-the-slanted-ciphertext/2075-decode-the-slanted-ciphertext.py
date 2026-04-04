class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cells = len(encodedText)
        cols = cells // rows
        mat = [list(encodedText[i*cols : i*cols + cols]) for i in range(rows)]
        decoded = ''
        for c in range(cols):
            i = 0
            j = c
            while i < rows and j < cols:
                decoded += mat[i][j]
                i += 1
                j += 1
        decoded = decoded.rstrip()
        return decoded