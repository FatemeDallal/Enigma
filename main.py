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


def search_date(date):
    check = False
    with open("EnigmaFile.txt") as f:
        for line in batched(f, 5):
            if line[0] == "Date: " + date + "\n":
                plug = line[1][12:-2:].split(", ")
                plug_board = {}
                for i in range(len(plug)):
                    plug_board[plug[i][0]] = plug[i][1]
                    plug_board[plug[i][1]] = plug[i][0]
                rotor1 = line[2][9:-2:]
                rotor2 = line[3][9:-2:]
                rotor3 = line[4][9:-2:]
                enigma = Enigma(date, plug_board, rotor1, rotor2, rotor3)
                check = True
                break
    if check:
        return enigma
    else:
        return "not exist"


def de_code_letter(a):
    return ord(a) - 97


def de_code_rotor(a, rotor):
    return rotor[de_code_letter(a)]


def de_code_plugboard(a, plug):
    if plug.get(a) is None:
        return a
    else:
        return plug.get(a)

