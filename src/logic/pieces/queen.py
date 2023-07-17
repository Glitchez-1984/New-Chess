from .piece import Piece
import numpy as np

class Queen(Piece):
    def get_valid_moves(self, board):
        possible_moves = []
        position = np.where(board == self)
        row, col = position[0][0], position[1][0]

        # Helper function to check if the square is on the board and empty
        def is_valid_square(r, c):
            return 0 <= r < 8 and 0 <= c < 8 and board[r, c] == 0

        # Diagonal moves
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while is_valid_square(r, c):
                possible_moves.append((r, c))
                r += dr
                c += dc

            # Check for captures
            if 0 <= r < 8 and 0 <= c < 8 and isinstance(board[r, c], Queen) and board[r, c].white != self.white:
                possible_moves.append((r, c))

        # Vertical and horizontal moves
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while is_valid_square(r, c):
                possible_moves.append((r, c))
                r += dr
                c += dc

            # Check for captures
            if 0 <= r < 8 and 0 <= c < 8 and isinstance(board[r, c], Queen) and board[r, c].white != self.white:
                possible_moves.append((r, c))

        return possible_moves