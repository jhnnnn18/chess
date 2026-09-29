# chess

A small chess engine in Python, built step by step as a learning project.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The [`chess`](https://python-chess.readthedocs.io/) library (python-chess)
handles the rules: legal moves, check, castling, en passant, and so on. That
leaves us free to focus on the engine's "brain".

## Play

```bash
python play.py            # you play White
python play.py --black    # you play Black
```

Enter moves like `e4`, `Nf3`, `O-O` or `e2e4`. Type `help` for commands.
Uppercase letters are White pieces and lowercase are Black.

## Test

```bash
pytest
```

## Roadmap

Every engine exposes `choose_move(board) -> chess.Move`, so `play.py` stays the
same while the engine gets smarter.

- [x] **1. Random mover:** plays any legal move (`engine/random_mover.py`)
- [ ] **2. Evaluation:** material and piece-square tables, 1-move lookahead
- [ ] **3. Minimax:** look several moves ahead
- [ ] **4. Alpha-beta pruning:** the same answer as minimax, much faster
- [ ] **5. Quiescence search:** stop "horizon effect" blunders
- [ ] **6. Iterative deepening and time control**
- [ ] **7. UCI protocol:** plug into chess GUIs
- [ ] **8. Transposition table:** remember positions already searched
- [ ] **9. (Optional) Own move generator:** replace python-chess, verified with perft
