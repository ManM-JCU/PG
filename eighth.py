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

if __name__ == "__main__":
    print(bin_to_dec("0"))
    print(bin_to_dec(1))
    print(bin_to_dec("100"))
    print(bin_to_dec(101))
    print(bin_to_dec("010101"))
    print(bin_to_dec(10000000))