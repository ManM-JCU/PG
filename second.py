def cislo_na_slovo(cislo):
    """Převede číslo (0-100) na český slovní zápis"""

jednotky = {
    0: "nula",
    1: "jedna",
    2: "dvě",
    3: "tři",
    4: "čtyři", 
    5: "pět",
    6: "šest",
    7: "sedm",
    8: "osm",
    9: "devět",
}

desitky = {
    10: "deset",
    20: "dvacet",
    30: "třicet",
    40: "čtyřicet",
    50: "padesát",
    60: "šedesát",
    70: "sedmdesát",
    80: "osmdesát",
    90: "devadesát",
}

teen = {
    11: "jedenáct",
    12: "dvanáct",
    13: "třináct",
    14: "čtrnáct",
    15: "patnáct",
    16: "šestnáct",
    17: "sedmnáct",
    18: "osmnáct",
    19: "devatenáct",
}

#Logika převodu
if cislo in jednotky:
    return jednotky[cislo]
elif cislo in teen:
    return teen[cislo]
elif cislo in desitky:
    return desitky[cislo]
elif 21 <= cislo < 100:
    d = (cislo// 10) * 10
    j = cislo % 10
    return f"{desitky[d]} {jednotky[j]}"
elif cislo == 100:
    return "sto"
else:
    return "Číslo není v rozsahu od 0 do 100."

#Zadání čísla
cislo = int(input("Zadej číslo: "))

#vysledek
vysledek = cislo_na_slovo(cislo)
print(f"Číslo {ciisloo} slovně: {vysledek}")
