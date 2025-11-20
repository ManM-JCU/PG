def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    start = figurka["pozice"]

    sx, sy = start
    cx, cy = cilova_pozice

    dx = cx - sx
    dy = cy - sy

    # 1) Cílová pozice musí být na šachovnici
    if not (1 <= cx <= 8 and 1 <= cy <= 8):
        return False

    # 2) Cílová pozice nesmí být obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Pomocná funkce: kontrola cesty
    def cesta_volna(start, cil):
        x, y = start
        tx, ty = cil
        stepx = (tx > x) - (tx < x)
        stepy = (ty > y) - (ty < y)

        x += stepx
        y += stepy
        while (x, y) != (tx, ty):
            if (x, y) in obsazene_pozice:
                return False
            x += stepx
            y += stepy
        return True

    # 3) Pravidla pohybu figur
    if typ == "pěšec":
        # pěšec jde jen nahoru (zvyšuje se řádek)
        # jeden krok
        if dx == 1 and dy == 0:
            if cilova_pozice not in obsazene_pozice:
                return True

        # dva kroky z výchozí pozice (řádek 2)
        if sx == 2 and dx == 2 and dy == 0:
            # musí být volná obě pole
            if (sx + 1, sy) not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
                return True

        return False

    if typ == "jezdec":
        return (abs(dx), abs(dy)) in [(1, 2), (2, 1)]

    if typ == "věž":
        if dx == 0 or dy == 0:
            return cesta_volna(start, cilova_pozice)
        return False

    if typ == "střelec":
        if abs(dx) == abs(dy):
            return cesta_volna(start, cilova_pozice)
        return False

    if typ == "dáma":
        if dx == 0 or dy == 0 or abs(dx) == abs(dy):
            return cesta_volna(start, cilova_pozice)
        return False

    if typ == "král":
        return max(abs(dx), abs(dy)) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
