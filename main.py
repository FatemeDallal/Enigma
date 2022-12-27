from itertools import islice


def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


# .........................................................................................

class Enigma:
    def __init__(self, date, plug_board, rotor1, rotor2, rotor3):
        self.date = date
        self.plug_board = plug_board
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3