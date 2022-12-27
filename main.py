from itertools import islice


def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


# .........................................................................................

alpha = "abcdefghijklmnopqrstuvwxyz"


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

                r1 = line[2][9:-2:]
                rotor1 = {}
                for i in range(len(alpha)):
                    rotor1[alpha[i]] = r1[i]

                r2 = line[3][9:-2:]
                rotor2 = {}
                for i in range(len(alpha)):
                    rotor2[alpha[i]] = r2[i]

                r3 = line[4][9:-2:]
                rotor3 = {}
                for i in range(len(alpha)):
                    rotor3[alpha[i]] = r3[i]

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
    return rotor.get(a)


def in_code_rotor(a, rotor):
    for i in rotor:
        if rotor.get(i) == a:
            return i


def de_code_plugboard(a, plug):
    if plug.get(a) is None:
        return a
    else:
        return plug.get(a)


def de_code_reflector(a):
    return chr(97 + (25 - de_code_letter(a)))


def shift_rotor(rotor):

    s = ""

    for i in rotor:
        s += rotor.get(i)

    shift_s = s[-1]
    for i in range(len(s) - 1):
        shift_s += s[i]

    d = {}

    for i in range(len(alpha)):
        d[alpha[i]] = shift_s[i]

    return d


if __name__ == '__main__':
    print("Enter Date .")
    date = input()

    print("Enter the input .")
    entry = input()

    if search_date(date) != "not exit":
        enigma = search_date(date)

        answer = []

        cnt = 0

        for i in entry:
            # Plug Board
            i = de_code_plugboard(i, enigma.plug_board)

            # rotor3
            i = de_code_rotor(i, enigma.rotor3)

            # rotor2
            i = de_code_rotor(i, enigma.rotor2)

            # rotor1
            i = de_code_rotor(i, enigma.rotor1)

            # reflector
            i = de_code_reflector(i)

            # rotor1
            i = in_code_rotor(i, enigma.rotor1)

            # rotor2
            i = in_code_rotor(i, enigma.rotor2)

            # rotor3
            i = in_code_rotor(i, enigma.rotor3)

            # Plug Board
            i = de_code_plugboard(i, enigma.plug_board)

            answer.append(i)

            if cnt < 26:
                # shift rotor3
                enigma.rotor3 = dict(shift_rotor(enigma.rotor3))
                cnt += 1

            elif cnt < 52:
                # shift rotor2
                enigma.rotor2 = dict(shift_rotor(enigma.rotor2))
                cnt += 1

            elif cnt < 78:
                # shift rotor1
                enigma.rotor1 = dict(shift_rotor(enigma.rotor1))
                cnt += 1

            elif cnt == 78:
                cnt = 0
                # shift rotor3
                shift_rotor(enigma.rotor3)
                cnt += 1

        for i in answer:
            print(i, end="")

    else:
        print("not exit")





