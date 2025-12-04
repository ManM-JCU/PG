def dec_to_bin(cislo):
    # číslo může být předáno jako str nebo int → převedeme na int
    num = int(cislo)

    # speciální případ
    if num == 0:
        return "0"

    result = ""

    # opakované dělení čísla dvěma
    while num > 0:
        bit = num % 2               # zbytky dávají bity
        result = str(bit) + result  # přidáváme bit zleva
        num = num // 2              # posun doprava

    return result


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
