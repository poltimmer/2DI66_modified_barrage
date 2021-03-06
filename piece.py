from __future__ import annotations

from enums.piecetype import PieceType
from enums.direction import Direction
from enums.player import Player
import board
import move

Board = lambda: board.Board
Move = lambda *args: move.Move(*args)


class Piece:
    def __init__(self, player: Player, piece_type: PieceType, x: int, y: int):
        self.board = None  # Will be filled by the board itself
        self.player = player
        self.piece_type = piece_type
        self.x = x
        self.y = y

    def get_available_moves(self) -> [Move]:
        """
        Return an array of all moves that can be done, taking into account
        - Its ability to move
        - Not moving out of bounds
        - Not moving into a piece of the same player
        """
        if not self.piece_type.can_move():
            return []

        directions = [Direction.UP, Direction.DOWN]
        if self.player == Player.RED:
            directions.append(Direction.RIGHT)
        else:
            directions.append(Direction.LEFT)
        moves = []
        for direction in directions:
            new_y = self.y + direction.get_dy()
            if new_y < 0 or new_y >= self.board.height:
                continue
            new_x = self.x + direction.get_dx()
            if new_x < 0 or new_x >= self.board.width:
                continue

            piece_on_new_pos = self.board.get_piece(new_x, new_y)
            if not piece_on_new_pos or piece_on_new_pos.player != self.player:
                moves.append(Move(self, new_x, new_y))
        return moves

    def __str__(self):
        return str(self.player) + ": " + str(self.piece_type)
