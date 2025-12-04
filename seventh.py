from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Pawn moves 1 square forward depending on color:
        - white: row increases (row + 1)
        - black: row decreases (row - 1)
        Only straight forward moves (no captures, no double-step, no en-passant).
        """
        row, col = self.position
        moves = []
        if self.color == 'white':
            new_pos = (row + 1, col)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
        else:  # black
            new_pos = (row - 1, col)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Diagonální pohyb do všech čtyř směrů až na okraj šachovnice.
        """
        row, col = self.position
        moves = []

        # směry: (delta_row, delta_col)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Pohyb po řadách a sloupcích (horizontálně a vertikálně) až na okraj šachovnice.
        """
        row, col = self.position
        moves = []

        # horizontálně vpravo
        c = col + 1
        while c <= 8:
            moves.append((row, c))
            c += 1
        # horizontálně vlevo
        c = col - 1
        while c >= 1:
            moves.append((row, c))
            c -= 1
        # vertikálně nahoru (zvyšování řádku)
        r = row + 1
        while r <= 8:
            moves.append((r, col))
            r += 1
        # vertikálně dolů (snižování řádku)
        r = row - 1
        while r >= 1:
            moves.append((r, col))
            r -= 1

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Kombinace tahu střelce (diagonály) a věže (řady/sloupce).
        """
        # využijeme implementace Bishop a Rook "manuálně"
        row, col = self.position
        moves = []

        # diagonály (stejně jako Bishop)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc

        # horizontály a vertikály (stejně jako Rook)
        c = col + 1
        while c <= 8:
            moves.append((row, c))
            c += 1
        c = col - 1
        while c >= 1:
            moves.append((row, c))
            c -= 1
        r = row + 1
        while r <= 8:
            moves.append((r, col))
            r += 1
        r = row - 1
        while r >= 1:
            moves.append((r, col))
            r -= 1

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Král se může pohnout o jedno políčko ve všech směrech.
        """
        row, col = self.position
        candidates = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [pos for pos in candidates if self.is_position_on_board(pos)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # krátké demo / testování
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 2)),
        Knight("black", (1, 2)),
        Bishop("white", (4, 4)),
        Rook("white", (1, 1)),
        Queen("black", (4, 1)),
        King("white", (8, 8))
    ]

    for p in pieces:
        print(p)
        print(p.possible_moves())
        print()
