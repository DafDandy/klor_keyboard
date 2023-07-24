import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
    )
    row_pins = (
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19
    )
    diode_orientation = DiodeOrientation.COLUMNS
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,                          5,  6,  7,  8,  9,
    10, 11, 12, 13, 14, 15,                         16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27,     28,         29,     32, 33, 34, 35, 36, 37,
                38, 39, 40, 41,                 42, 43, 44, 45
    ]