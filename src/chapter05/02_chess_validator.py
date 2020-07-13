#! /usr/bin/env python3
# Chess validator


class ChessException(Exception):
    pass


def chess_dictionary_validator(chess_dict: dict):
    for position, piece in chess_dict.items():
        print(f"position ({position}): piece({piece})")


def validate_position(position):
    size = len(position)
    if size != 2:
        raise ChessException(f"Invalid length({size}) for position ({position}). Expected 2")
    row = position[0]
    if row not in "12345678":
        raise ChessException(f"Invalid row number: {row}. Expected values: 1-8")
    column = position[1]
    if column not in "abcdefgh":
        raise ChessException(f"Invalid column value: {column}. Expected values: a-h")
    return row, column


def validate_piece(piece):
    size = len(piece)
    if size < 5:
        raise ChessException(f"Invalid length({size}) for piece ({piece}). Expected at least 5 characters")
    color = piece[0]
    if color not in ["w", "b"]:
        raise ChessException(f"Invalid color: {color}. 'b' for 'Black' and 'w' for 'White'")
    piece_name = piece[1:]
    valid_pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
    if piece_name not in valid_pieces:
        raise ChessException(f"Invalid piece name: {piece_name}. Expected values: {','.join(valid_pieces)}")
    return color, piece_name


chess = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking"
}

chess_dictionary_validator(chess)

for k, v in chess.items():
    print(f"{k}: {validate_position(k)} -- {validate_piece(v)}")
try:
    validate_position("1m")
except ChessException as e:
    print(e)
