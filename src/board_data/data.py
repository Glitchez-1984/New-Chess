import numpy as np
import sys

sys.path.append('..')
from src.constants import Board
from src.logic.pieces.knight import Knight
from src.logic.pieces.pawn import Pawn
from src.logic.pieces.bishop import Bishop
from src.logic.pieces.rook import Rook
from src.logic.pieces.queen import Queen
from src.logic.pieces.king import King

board = np.zeros((Board.SIZE.value, Board.SIZE.value), dtype=object)
board[0, 7] = Rook(True, (0, 700), 3)
board[1, 7] = Knight(True, (100, 700), 1)
board[2, 7] = Bishop(True, (200, 700), 2)
board[3, 7] = Queen(True, (300, 700), 4)
board[4, 7] = King(True, (400, 700), 5)
board[5, 7] = Bishop(True, (500, 700), 2)
board[6, 7] = Knight(True, (600, 700), 1)
board[7, 7] = Rook(True, (700, 700), 3)
board[0, 6] = Pawn(True, (0, 600), 0)
board[1, 6] = Pawn(True, (100, 600), 0)
board[2, 6] = Pawn(True, (200, 600), 0)
board[3, 6] = Pawn(True, (300, 600), 0)
board[4, 6] = Pawn(True, (400, 600), 0)
board[5, 6] = Pawn(True, (500, 600), 0)
board[6, 6] = Pawn(True, (600, 600), 0)
board[7, 6] = Pawn(True, (700, 600), 0)

selected_piece = None
possible_moves = []
