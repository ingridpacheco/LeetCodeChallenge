# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
# Here are the rules of Tic-Tac-Toe:
# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

# Ex:
#   Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
#   Output: "A"

# Possibilidades pra ganhar:
            # x é igual nas três jogadas de um jogador
            # y é igual nas //
            # x = y nas três jogadas de um jogador

        # [[0,0],[2,0],[1,1],[2,1],[2,2]]

        # X - O
        # - X O
        # - - X => A wins

        # [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]

        # X X O => [0,0],[0,1],[0,2]
        # X O -    [1,0], [1,1], [1,2]
        # O - - => B wins

        # [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]

        # X O X
        # X O O
        # O X X => Draw

        # [[0,0],[1,1]]

        # X - -
        # - O -
        # - - - => Pending
        
        # [[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]
        
        # O X -
        # X X X
        # O O -

# Solution 1

class Solution(object):
    
    def check_winner(self, moves):
        if len(moves) < 3:
            return False
        
        if (moves[0][0] == moves[1][0]) and (moves[1][0] == moves[2][0]):
            return True

        if (moves[0][1] == moves[1][1]) and (moves[1][1] == moves[2][1]):
            return True

        if (moves[0][0] == moves[0][1]) and (moves[1][0] == moves[1][1]) and (moves[2][0] == moves[2][1]):
            return True

        for move in moves:
            if (move != [0,2] and move != [1,1] and move != [2,0]):
                return False

        return True   
    
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
    
        if len(moves) < 5:
            return "Pending"
        
        A = moves[::2]
        
        if (len(A) > 3):
            for i in range(0,len(A)):
                for j in range(1,len(A)):
                    if i != j:
                        for k in range(2,len(A)):
                            if k != j and k != i:
                                new_A = [A[i],A[j],A[k]]
                                if (self.check_winner(new_A)):
                                    return "A"
        else:
            if (self.check_winner(A)):
                return "A"
        
        B = moves[1::2]
        
        if (len(B) > 3):
            for i in range(0,len(B)):
                for j in range(1,len(B)):
                    if i != j:
                        for k in range(2,len(B)):
                            if k != j and k != i:
                                new_B = [B[i],B[j],B[k]]
                                if (self.check_winner(new_B)):
                                    return "B"
        else:
            if (self.check_winner(B)):
                return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"

# Solution 2

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        board = [[0] * 3 for _ in range(3)]
        
        def check_winner(row, col, p):

            if (board[row][0] == board[row][1]) and (board[row][1] == board[row][2]) and (board[row][0] == p):
                return True

            if (board[0][col] == board[1][col]) and (board[1][col] == board[2][col]) and (board[0][col] == p):
                return True

            if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] == p):
                return True
            
            if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] == p):
                return True 
        
            return False
        
        if len(moves) < 5:
            return "Pending"
        
        p = 'A'

        for move in moves:
            row, col = move
            board[row][col] = p
            if check_winner(row, col, p):
                return p
            
            p = 'B' if p == 'A' else 'A'
        
        return "Draw" if len(moves) == 9 else "Pending"