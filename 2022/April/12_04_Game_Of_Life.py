class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        new_board = [[0 for k in range(len(board[0]))] for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                living = 0
                
                if i != 0:
                    living += board[i-1][j]
                    if j != 0:
                        living += board[i-1][j-1]
                    if j!= len(board[i]) - 1:
                        living += board[i-1][j+1]
                
                if i != len(board) - 1:
                    living += board[i+1][j]
                    if j != 0:
                        living += board[i+1][j-1]
                    if j!= len(board[i]) - 1:
                        living += board[i+1][j+1]
                    
                if j != 0:
                    living += board[i][j-1]
                if j != len(board[i]) - 1:
                    living += board[i][j+1]
                    
                if (board[i][j] == 1 and (living == 2 or living == 3)) or board[i][j] == 0 and living == 3:
                        new_board[i][j] = 1

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = new_board[i][j]