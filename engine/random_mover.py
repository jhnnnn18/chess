"""Step 1: the simplest possible "engine" - pick any legal move at random.

Every engine we build will expose the same function:

    choose_move(board) -> chess.Move

That way play.py never needs to change; later steps just swap in a smarter
choose_move (one that evaluates positions and searches ahead).
"""

import random

import chess


def choose_move(board: chess.Board) -> chess.Move:
    """Return a random legal move for the side to move.

    `board.legal_moves` is provided by python-chess. It already handles all the
    tricky rules: check, pins, castling, en passant and promotion.
    """
    moves = list(board.legal_moves)
    if not moves:
        raise ValueError("No legal moves: the game is already over.")
    return random.choice(moves)
