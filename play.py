"""Play against the engine in your terminal.

    python play.py            # you play White
    python play.py --black    # you play Black

Enter moves in standard notation (e4, Nf3, O-O, exd5, e8=Q) or in UCI
notation (e2e4, g1f3, e7e8q). Type "help" for other commands.
"""

import argparse

import chess

from engine.random_mover import choose_move

HELP = """Commands:
  <move>   a move like e4, Nf3, O-O or e2e4
  moves    list your legal moves
  undo     take back your last move (and the engine's reply)
  fen      print the current position as a FEN string
  quit     leave the game"""


def render(board: chess.Board, as_white: bool) -> str:
    """Draw the board with rank and file labels, from the player's side."""
    ranks = range(7, -1, -1) if as_white else range(8)
    files = range(8) if as_white else range(7, -1, -1)
    lines = []
    for rank in ranks:
        row = []
        for file in files:
            piece = board.piece_at(chess.square(file, rank))
            row.append(piece.symbol() if piece else ".")
        lines.append(f"{rank + 1}  " + " ".join(row))
    lines.append("   " + " ".join(chess.FILE_NAMES[f] for f in files))
    return "\n".join(lines)


def parse_move(board: chess.Board, text: str) -> chess.Move | None:
    """Accept standard (SAN) or UCI notation; return None if illegal or unreadable."""
    for parse in (board.parse_san, board.parse_uci):
        try:
            return parse(text)
        except ValueError:
            continue
    return None


def human_turn(board: chess.Board) -> bool:
    """Handle one line of input. Returns False if the player wants to quit."""
    while True:
        try:
            text = input("Your move: ").strip()
        except EOFError:  # Ctrl-D
            return False
        if text in ("quit", "exit"):
            return False
        if text == "help":
            print(HELP)
        elif text == "moves":
            print(" ".join(sorted(board.san(m) for m in board.legal_moves)))
        elif text == "fen":
            print(board.fen())
        elif text == "undo":
            # Pop the engine's reply and our own move, if there are two to pop.
            if len(board.move_stack) >= 2:
                board.pop()
                board.pop()
                return True
            print("Nothing to undo.")
        else:
            move = parse_move(board, text)
            if move is None:
                print(f"'{text}' is not a legal move here. Type 'moves' to see options.")
                continue
            board.push(move)
            return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Play chess against the engine.")
    parser.add_argument("--black", action="store_true", help="play as Black")
    args = parser.parse_args()

    human_color = chess.BLACK if args.black else chess.WHITE
    board = chess.Board()
    print("Type 'help' for commands.\n")

    while not board.is_game_over():
        print(render(board, as_white=human_color == chess.WHITE), "\n")
        if board.turn == human_color:
            if not human_turn(board):
                print("Bye!")
                return
        else:
            move = choose_move(board)
            print(f"Engine plays {board.san(move)}\n")
            board.push(move)

    print(render(board, as_white=human_color == chess.WHITE), "\n")
    outcome = board.outcome()
    if outcome.winner is None:
        print(f"Draw ({outcome.termination.name.lower().replace('_', ' ')}).")
    else:
        winner = "You win" if outcome.winner == human_color else "Engine wins"
        print(f"{winner} by {outcome.termination.name.lower()}! Result: {board.result()}")


if __name__ == "__main__":
    main()
