import chess
import pytest

from engine.random_mover import choose_move


def test_returns_a_legal_move_from_start():
    board = chess.Board()
    assert choose_move(board) in board.legal_moves


def test_finds_the_only_legal_move():
    # Black king on h8 is in check from the queen on h6 and has one escape: g8.
    board = chess.Board("7k/8/7Q/8/8/8/8/K7 b - - 0 1")
    assert choose_move(board) == chess.Move.from_uci("h8g8")


def test_raises_when_checkmated():
    # Fool's mate: White is checkmated and has no moves.
    board = chess.Board()
    for san in ["f3", "e5", "g4", "Qh4#"]:
        board.push_san(san)
    with pytest.raises(ValueError):
        choose_move(board)


def test_self_play_always_finishes_with_legal_moves():
    board = chess.Board()
    while not board.is_game_over(claim_draw=True):
        move = choose_move(board)
        assert move in board.legal_moves
        board.push(move)
