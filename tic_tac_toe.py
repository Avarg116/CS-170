
import random

class TTT_cs170_judge:
    def __init__(self):
        self.board = []
        
    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)
            
    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()
            
    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        
        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True
        
        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True
        
        return False
    
    def is_board_full(self): # Check if the game board is full
        return all([cell in ['X', 'O'] for row in self.board for cell in row])
    
class Player_1:
    def __init__(self, judge):
        self.board = judge.board
    
    def my_play(self): # Player 1's move
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())
            
            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                self.board[row-1][col-1] = 'X'
                break
            else:
                print("Wrong coordination!")


class Player_2:
    def __init__(self, judge):
        self.judge = judge
        self.board = judge.board

    def my_play(self): # Player 2's move using minimax algorithm
       high_score, best_move = self.minimax(self.board, True, float('-inf'), float('inf'))
       row, col = best_move
       self.board[row][col] = 'O'

    def minimax(self, board, maximizing, alpha, beta):
        if self.judge.is_winner('X'):
            return -1, None
        if self.judge.is_winner('O'):
            return 1, None
        if self.judge.is_board_full():
            return 0, None

        high_score = float('-inf') if maximizing else float('inf')

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '-':
                    board[row][col] = 'O' if maximizing else 'X'
                    score, _ = self.minimax(board, not maximizing, alpha, beta)
                    board[row][col] = '-'

                    if maximizing:
                        if score > high_score:
                            high_score = score
                            best_move = row, col
                        if score > alpha:
                            alpha = score
                    else:
                        if score < high_score:
                            high_score = score
                            best_move = row, col
                        if score < beta:
                            beta = score

                    if maximizing and high_score >= beta:
                        break
                    elif not maximizing and high_score <= alpha:
                        break

        return high_score, best_move
    
# Main Game Loop
def game_loop():
    n = 3  # Board size
    game = TTT_cs170_judge()
    game.create_board(n)
    player1 = Player_1(game)
    player2 = Player_2(game)
    starter = random.randint(0, 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()
        while not win:
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
    else:
        print("Player 2 starts.")
        game.display_board()
        while not win:
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
            
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
