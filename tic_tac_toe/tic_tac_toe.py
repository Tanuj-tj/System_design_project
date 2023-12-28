from model.player import Player
from model.board import Board
from model.playing_piece_x import PyaingPieceX
from model.playing_piece_o import PyaingPieceO
from collections import deque

class TicTacToeGame:

    def __init__(self):
        self.players = deque() 
        self.game_board = Board(size=3)
        self.initialize_game()

    def initialize_game(self):
        
        # Creating 2 players
        cross_piece: PyaingPieceX = PyaingPieceX()
        player1: Player = Player(name="Player1", playing_piece=cross_piece)
        noughts_piece: PyaingPieceO = PyaingPieceO()
        player2: Player = Player(name="Player2", playing_piece=noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

    def start_game(self):

        no_winner: bool = True
        while no_winner:
            player_turn: Player = self.players.popleft()
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            # Read the user input
            print("Player:", player_turn.name, "Enter row,column: ")
            s = input()
            values = s.split(",")
            input_row = int(values[0])
            input_column = int(values[1])

            # Place the piece
            piece_added_successfully = self.game_board.add_piece(input_row, input_column, player_turn.playing_piece)
            if not piece_added_successfully:
                # Player cannot insert the piece into this cell, player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            winner = self.is_there_winner(input_row, input_column, player_turn.playing_piece.piece_type)
            if winner:
                return player_turn.name

        return "tie"
    
    def is_there_winner(self, row, column, piece_type):
        row_match = all(self.game_board.board[row][i] == piece_type for i in range(self.game_board.size))
        column_match = all(self.game_board.board[i][column] == piece_type for i in range(self.game_board.size))
        diagonal_match = all(self.game_board.board[i][i] == piece_type for i in range(self.game_board.size))
        anti_diagonal_match = all(self.game_board.board[i][self.game_board.size - 1 - i] == piece_type for i in range(self.game_board.size))

        return row_match or column_match or diagonal_match or anti_diagonal_match

            