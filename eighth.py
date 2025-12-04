def bin_to_dec(binarni_cislo):
    #binarni cislo muze prijit jako int nebo str -> prevedeme vse na str
    bin_str = str(binarni_cislo)

    #vysledna desitkova honota
    decimal_value = 0

    #projdeme vsechny bity zleva doprava
    for bit in bin_str:
        #posuneme dosavadni hodnotu doleva (vynasobime 2)
        decimal_value = decimal_value * 2
        #pricteme aktualni bit (0 nebo 1)
        decimal_value += int(bit)

    return decimal_value 