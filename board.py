

class Pawn:
    def __init__(self, color):
        self.color = color
        self.type = "p"

    def moves(self):
        return [(-1, 1), (0, 1), (0, 2), (1, 1)]


class Rook:
    def __init__(self, color):
        self.color = color
        self.type = "R"

    def moves(self):
        return [(-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, -7),
                (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2),
                (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0),
                (5, 0), (6, 0), (7, 0)]


class Bishop:
    def __init__(self, color):
        self.color = color
        self.type = "B"

    def moves(self):
        return [(-7, -7), (-7, 7), (-6, -6), (-6, 6), (-5, -5), (-5, 5), (-4, -4),
                (-4, 4), (-3, -3), (-3, 3), (-2, -2), (-2, 2), (-1, -1), (-1, 1),
                (1, -1), (1, 1), (2, -2), (2, 2), (3, -3), (3, 3), (4, -4), (4, 4),
                (5, -5), (5, 5), (6, -6), (6, 6), (7, -7), (7, 7)]

class Knight:
    def __init__(self, color):
        self.color = color
        self.type = "N"


    def moves(self):
        return [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

class King:
    def __init__(self, color):
        self.color = color
        self.type = "K"

    def moves(self):
        return [(-1, -1), (-1, 0), (-1, 1),(0, -4), (0, -1), (0, 1), (0, 3), (1, -1), (1, 0), (1, 1)]

class Queen:
    def __init__(self, color):
        self.color = color
        self.type = "Q"

    @property
    def moves(self):
        return [Rook.moves() + Bishop.moves()]
class Cell:
    def __init__(self, loc, piece=None):
        self.loc = loc
        self.piece = piece

class Loc:
    def __init__(self, xy, acn, col):
        self.xy = xy
        self.acn = acn
        self.col = col


# priority queue
class Board:
    d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    f = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

    z = {(0, 0): "a1", (0, 1): "a2", (0, 2): "a3", (0, 3): "a4", (0, 4): "a5", (0, 5): "a6", (0, 6): "a7", (0, 7): "a8", (1, 0): "b1", (1, 1): "b2", (1, 2): "b3", (1, 3): "b4", (1, 4): "b5", (1, 5): "b6", (1, 6): "b7", (1, 7): "b8", (2, 0): "c1", (2, 1): "c2", (2, 2): "c3", (2, 3): "c4", (2, 4): "c5", (2, 5): "c6", (2, 6): "c7", (2, 7): "c8", (3, 0): "d1", (3, 1): "d2", (3, 2): "d3", (3, 3): "d4", (3, 4): "d5", (3, 5): "d6", (3, 6): "d7", (3, 7): "d8", (4, 0): "e1", (4, 1): "e2", (4, 2): "e3", (4, 3): "e4", (4, 4): "e5", (4, 5): "e6", (4, 6): "e7", (4, 7): "e8", (5, 0): "f1", (5, 1): "f2", (5, 2): "f3", (5, 3): "f4", (5, 4): "f5", (5, 5): "f6", (5, 6): "f7", (5, 7): "f8", (6, 0): "g1", (6, 1): "g2", (6, 2): "g3", (6, 3): "g4", (6, 4): "g5", (6, 5): "g6", (6, 6): "g7", (6, 7): "g8", (7, 0): "h1", (7, 1): "h2", (7, 2): "h3", (7, 3): "h4", (7, 4): "h5", (7, 5): "h6", (7, 6): "h7", (7, 7): "h8" }
    r = {"a1": (0, 0), "a2": (0, 1), "a3": (0, 2), "a4": (0, 3), "a5": (0, 4), "a6": (0, 5), "a7": (0, 6), "a8": (0, 7), "b1": (1, 0), "b2": (1, 1), "b3": (1, 2), "b4": (1, 3), "b5": (1, 4), "b6": (1, 5), "b7": (1, 6), "b8": (1, 7), "c1": (2, 0), "c2": (2, 1), "c3": (2, 2), "c4": (2, 3), "c5": (2, 4), "c6": (2, 5), "c7": (2, 6), "c8": (2, 7), "d1": (3, 0), "d2": (3, 1), "d3": (3, 2), "d4": (3, 3), "d5": (3, 4), "d6": (3, 5), "d7": (3, 6), "d8": (3, 7), "e1": (4, 0), "e2": (4, 1), "e3": (4, 2), "e4": (4, 3), "e5": (4, 4), "e6": (4, 5), "e7": (4, 6), "e8": (4, 7), "f1": (5, 0), "f2": (5, 1), "f3": (5, 2), "f4": (5, 3), "f5": (5, 4), "f6": (5, 5), "f7": (5, 6), "f8": (5, 7), "g1": (6, 0), "g2": (6, 1), "g3": (6, 2), "g4": (6, 3), "g5": (6, 4), "g6": (6, 5), "g7": (6, 6), "g8": (6, 7), "h1": (7, 0), "h2": (7, 1), "h3": (7, 2), "h4": (7, 3), "h5": (7, 4), "h6": (7, 5), "h7": (7, 6), "h8": (7, 7) }

    def __init__(self):
        self.states = []

        for i in range(0, 8):
            for j in range(0, 8):
                loc = self.f[i] + str(j+1)
                if i % 2 == 0:
                    bcol = "black" if j % 2 == 0 else "white"
                else:
                    bcol = "white" if j % 2 == 0 else "black"

                if j == 0 or j == 7:
                    col = 'white' if j == 0 else 'black'
                    if i == 0 or i == 7:
                        self.states.append(Cell(Loc((i, j), loc, bcol), Rook(col)))

                    elif i == 1 or i == 6:
                        self.states.append(Cell(Loc((i, j), loc, bcol), Knight(col)))

                    elif i == 2 or i == 5:
                        self.states.append(Cell(Loc((i, j), loc, bcol), Bishop(col)))

                    elif i == 3 and j == 0:
                        self.states.append(Cell(Loc((i, j), loc, bcol), Queen("white")))

                    elif i == 4 and j == 0:
                        self.states.append(Cell(Loc((i, j), loc, bcol), King("white")))

                    elif i == 3 and j == 7:
                        self.states.append(Cell(Loc((i, j), loc, bcol), Queen("black")))

                    else:
                        self.states.append(Cell(Loc((i, j), loc, bcol), King("black")))

                elif j == 1 or j == 6:
                    col = 'white' if j == 1 else 'black'
                    self.states.append(Cell(Loc((i, j), loc, bcol), Pawn(col)))
                else:
                    self.states.append(Cell(Loc((i, j), loc, bcol)))

        self.bQ = [self.states[31]]
        self.bK = [self.states[39]]
        self.bN = [self.states[15], self.states[55]]
        self.bB = [self.states[23], self.states[47]]
        self.bR = [self.states[7], self.states[63]]
        self.wQ = [self.states[24]]
        self.wK = [self.states[32]]
        self.wB = [self.states[16], self.states[40]]
        self.wN = [self.states[8], self.states[48]]
        self.wR = [self.states[0], self.states[56]]
        self.b = []
        self.w = []

        for i in range(0, 8):
            wp = i*8 + 1
            self.w.append(self.states[wp])
            self.b.append(self.states[wp + 5])

    def move(self, loc, nloc): #move piece at location (loc) to new location (nloc) piece type (ptype)
        f = 0
        n = 0
        for i in range(0,len(self.states)): # potential conflict if opposing sides can move to same square
            if self.states[i].loc.acn == loc:
                f = i

            if self.states[i].loc.acn == nloc:
                n = i
        self.states[n].piece = self.states[f].piece
        self.states[f].piece = None

    def pmove(self, nloc, col, pt, namb=None):
        if pt == "R":
            t = self.wR if col == True else self.bR
            movez = Rook.moves
        elif pt == "N":
            t = self.wN if col == True else self.bN
            movez = Knight.moves
        elif pt == "B":
            t = self.wB if col == True else self.bB
            movez = Bishop.moves
        elif pt == "Q":
            t = self.wQ if col == True else self.bQ
            movez = Queen.moves
        else:
            t = self.wK if col == True else self.bK
            movez = King.moves

        for p in t: # piece in temp
            if namb and p.loc[0] != namb or namb and p.loc[1] != namb:
                continue
            x = p.loc.xy[0]
            y = p.loc.xy[1]
            x2 = self.d[nloc[0]]
            y2 = int(nloc[1])

            for xyz in p.piece.moves():
                if x == xyz[0] + x2 and y == xyz[1] + y2:
                    self.move(str(self.f[xyz[0] + x2] + (xyz[1] + y2)), nloc)
                    break
                    #break might need to break twice

    def castle(self, col, qork):
        if col == "black":
            k = 39
            r = 7 if qork == "q" else 63
        else:
            k = 32
            r = 0 if qork == "q" else 56
        temp = self.states[k].piece
        self.states[k].piece = self.states[r].piece
        self.states[r].piece = temp
