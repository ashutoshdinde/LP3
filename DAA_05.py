
def solveNQueens(n: int, first_queen_col: int):
    board = [["." for _ in range(n)] for _ in range(n)]
    
    board[0][first_queen_col] = "Q"
    def is_safe(row, col):
        for r in range(row):
            if board[r][col] == "Q": 
                return False
            if col - (row - r) >= 0 and board[r][col - (row - r)] == "Q":  
                return False
            if col + (row - r) < n  and board[r][col + (row - r)] == "Q":  
                return False
        return True

    def backtrack(row):
        if row == n:
            return True
            
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"  
                if backtrack(row + 1):
                    return True  
                board[row][col] = "."  
        return False  
    backtrack(1)

    return board

if __name__ == "__main__":
    n = 8
    first_queen_col = 1  
    board = solveNQueens(n, first_queen_col)

    for row in board:
        print(" ".join(row))
