import chess
import chess.pgn
import io


def convert(uci_moves:list):
    board = chess.Board()
    game = chess.pgn.Game()
    node = game

    for uci in uci_moves:
        move = chess.Move.from_uci(uci)
        if move in board.legal_moves:
            board.push(move)
            node = node.add_variation(move)
        else:
            raise ValueError(f"{move} is invalid.")

    # Export PGN
    pgn_io = io.StringIO()
    print(game, file=pgn_io)
    pgn_text = pgn_io.getvalue()

    return pgn_text