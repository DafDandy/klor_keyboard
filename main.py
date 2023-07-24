from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

split = Split(
    data_pin=keyboard.data_pin
    # data_pin2=keyboard.data_pin2
)
keyboard.modules.append(split)

L1_SPC = KC.LT(1, KC.SPC)
L2_ENT = KC.LT(2, KC.ENT)
S_BSPC = KC.HT(KC.BSPC, KC.LSFT)
C_DEL = KC.HT(KC.DEL, KC.LCTL)
M_END = KC.HT(KC.END, KC.MEH)
H_PGDN = KC.HT(KC.PGDN, KC.HYPER)

keyboard.keymap = [
    [   #0
                    KC.Q,   KC.W,    KC.F,    KC.P,   KC.G,                                         KC.J,   KC.L,    KC.U,  KC.Y,   KC.SCLN,
        KC.TAB,    KC.A,   KC.R,    KC.S,    KC.T,   KC.D,                                          KC.H,   KC.N,    KC.E,  KC.I,   KC.O,       KC.QUOT,
        KC.LSFT,    KC.Z,   KC.X,    KC.C,    KC.V,   KC.B, KC.LALT,                     KC.RALT,   KC.K,  KC.M, KC.COMM,  KC.DOT, KC.SLSH,    KC.RSFT,
                                    KC.LGUI, KC.LCTL, C_DEL, KC.BSLS,                   L1_SPC,    L2_ENT, KC.UP, KC.DOWN
    ]
    # ,[   #0
    #                 KC.Q,   KC.W,    KC.F,    KC.P,   KC.G,                                         KC.J,   KC.L,    KC.U,  KC.Y,   KC.SCLN,
    #     KC.TAB,    KC.A,   KC.R,    KC.S,    KC.T,   KC.D,                                          KC.H,   KC.N,    KC.E,  KC.I,   KC.O,       KC.QUOT,
    #     KC.LSFT,    KC.Z,   KC.X,    KC.C,    KC.V,   KC.B, KC.LALT,                     KC.RALT,   KC.K,  KC.M, KC.COMM,  KC.DOT, KC.SLSH,    KC.RSFT,
    #                                 KC.LGUI, KC.LCTL, C_DEL, KC.BSLS,                   L1_SPC,    L2_ENT, KC.UP, KC.DOWN
    # ]
    # ,[   #0
    #                 KC.Q,   KC.W,    KC.F,    KC.P,   KC.G,                                         KC.J,   KC.L,    KC.U,  KC.Y,   KC.SCLN,
    #     KC.TAB,    KC.A,   KC.R,    KC.S,    KC.T,   KC.D,                                          KC.H,   KC.N,    KC.E,  KC.I,   KC.O,       KC.QUOT,
    #     KC.LSFT,    KC.Z,   KC.X,    KC.C,    KC.V,   KC.B, KC.LALT,                     KC.RALT,   KC.K,  KC.M, KC.COMM,  KC.DOT, KC.SLSH,    KC.RSFT,
    #                                 KC.LGUI, KC.LCTL, C_DEL, KC.BSLS,                   L1_SPC,    L2_ENT, KC.UP, KC.DOWN
    # ]
]

if __name__ == '__main__':
    keyboard.go()